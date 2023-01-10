from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request,'polls/home.html')

def info(request):
    return render(request,'polls/info.html')

def password(request):
    
    characters= list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+='))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('select all'):
        characters.extend(list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+='))   

    length = int(request.GET.get('length',12))
    thepassword=''
    for x in range(length):
        thepassword+=random.choice(characters)

    return render(request,'polls/password.html', {'password':thepassword})

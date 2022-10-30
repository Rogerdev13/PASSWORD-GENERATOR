from django.shortcuts import render
#from django.shortcuts import HttpResponse
import random 

# Create your views here.
def about(request):
    return render(request , 'about.html')

def home(request):
    return render(request , 'home.html')

def password(request):

    characters = list('abcdabcdefghijklmnopqrstuvwxyz')
    password_final = ''

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUCWXYZ')
    
    if request.GET.get('specials'):
        characters.extend('!%$#/)*&')
    if request.GET.get('numbers'):
        characters.extend('123456789')

    length = int(request.GET.get('lenght'))
    for x in range(length):
        password_final += random.choice(characters)

    return render(request  , 'password.html' , {'password' : password_final})
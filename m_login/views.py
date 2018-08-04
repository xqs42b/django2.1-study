from django.shortcuts import render, HttpResponse, redirect 

# Create your views here.
def register(request):
    return render(request, 'm_login/register.html')

def login(request):
    return render(request, 'm_login/login.html')

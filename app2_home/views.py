from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def mainWindow(Request):
    return HttpResponse("<a href='http://127.0.0.1:8000/app1_home' target='blank'>Link to home page!</a><br><h1> Link to registration page</h1> <br>")
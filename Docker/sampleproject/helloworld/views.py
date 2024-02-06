# helloworld/views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect

def hello_world(request):
    return render(request, 'index.html')

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def venu(response):
    return HttpResponse('<h1><marquee>hi my name is venu gopal</h1></marquee>')

def jampandu(response):
    return HttpResponse('hi jampandu how are you')
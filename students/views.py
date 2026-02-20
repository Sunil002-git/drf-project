from django.shortcuts import render
from django.urls import path 
from django.http import HttpResponse

# Create your views here.

def students(request):
    students = [
        {
            'id' : 205209,
            'name' : 'Sunil',
            'Job' : "Web Dev"
        }
    ]
    return HttpResponse(students)
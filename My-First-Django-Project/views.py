from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world.welcome. This is my first django program")

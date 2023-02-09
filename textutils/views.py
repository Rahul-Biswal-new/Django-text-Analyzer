#  readymade file
from django.http  import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse('<h1>Hello</h1><a href="https://www.youtube.com/">this is my youtube channel</a>')
    params = {"name": "harry", "place": "usa" }
    return render(request, 'index.html' , params)
    # render has three arguments 1- request 2- file name 3- params

def about(request):
    return HttpResponse('<h1>this is about</h1>')

def removepunc(request):
    # get the text
    djtext = request.GET.get('text', 'default')
    print(djtext)
    # analyze the text
    return HttpResponse("reomve punc <a href='/'>back</a>")

def capitalizefirst(request):
    return HttpResponse("capitalize fist")

def newlineremove(request):
    return HttpResponse("newline remove ")

def spaceremover(request):
    return HttpResponse("space remover ")

def charcount(request):
    return HttpResponse("char count")
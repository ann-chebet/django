from django.shortcuts import render, HttpResponse


# Create your views here.
def test(request):
    return HttpResponse("this is my own django project")
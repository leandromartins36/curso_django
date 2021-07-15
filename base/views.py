from django.shortcuts import render
from django.shortcuts import HttpResponse

# Crete your views here.


def home(request):
    return HttpResponse('Ola! Django')

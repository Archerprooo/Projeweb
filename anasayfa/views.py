from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def anasayfafen(request):
  # return HttpResponse(f"Welcome to home page.{request}")
  return HttpResponse(f"Welcome to home page.{request}")

def anasayfaf(request):
  return HttpResponse("Ana sayfaya hoş geldiniz..")
  # return HttpResponse(f"Ana sayfaya hoş geldiniz..{request}")
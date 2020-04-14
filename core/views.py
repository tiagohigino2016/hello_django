from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome, idade))

def soma(request, valor1, valor2):
    resultado = valor1 + valor2
    return HttpResponse('<h1>A soma de {} e {} é {}</h1>'.format(valor1, valor2, resultado))







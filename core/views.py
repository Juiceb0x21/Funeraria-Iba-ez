from django.shortcuts import render, redirect


def index(request):
    return render(request, 'core/index.html')

def extra(request):
    return render(request, 'core/one-page.html')
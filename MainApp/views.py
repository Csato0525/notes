from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def VIEW (request):
    return render(request, 'index.html')


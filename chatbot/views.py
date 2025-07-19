from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.
@login_required
def home(request):
    return render(request, 'mainscreen/home.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def login_view(request):
    return render(request, 'account/login.html')

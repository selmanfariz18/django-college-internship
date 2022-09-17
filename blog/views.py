from django.shortcuts import render,redirect
from .models import User

# Create your views here.
from django.http import HttpResponse
def now(request):
    return HttpResponse('hi')
def first(request):
    return HttpResponse('hello')
def second(request):
    return HttpResponse('ajna')
def home(request):
    return render(request,'home.html')
def index(request):
    return render(request,'index.html')
def login(request):
    data=request.POST
    username=data.get("username")
    password=data.get("password")
    print(password)
    print(username)
    user=User.objects.get(username=username)
    print(user.username)
    print(user.password)
    usrname=user.username
    passwd=user.password
    if password==passwd and usrname==username:
        return render(request,'index.html')
    else:
        return HttpResponse('username or passwd incorrect')

def registration(request):
    data=request.POST
    username=data.get("username")
    password=data.get("password")
    roll_num=data.get("roll_num")
    if request.method=='POST':
        userdata=User()
        userdata.username=username
        userdata.password=password
        userdata.roll_num=roll_num
        userdata.save()
    return render(request,'registration.html',)
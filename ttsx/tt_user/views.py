# coding=utf-8
from hashlib import sha1
from django.shortcuts import render, redirect

# Create your views here.
from models import UserInfo


def register(request):
    context = {'title': '注册'}
    return render(request, 'tt_user/register.html', context)


def register_save(request):
    dict = request.POST
    uname = dict.get('user_name')
    upwd = dict.get('pwd')
    upwd2 = dict.get('cpwd')
    email = dict.get('email')
    if upwd != upwd2:
        return redirect('/user/register/')
    s1 = sha1()
    s1.update(upwd)
    upwd_sha1 = s1.hexdigest()

    user = UserInfo()
    user.uname = uname
    user.upwd = upwd_sha1
    user.uemail = email
    user.save()
    return redirect('/user/login/')


def login(request):
    context = {'title': '登陆'}
    return render(request, 'tt_user/login.html', context)

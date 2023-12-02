from django.shortcuts import render

def hm(response):
    return render(response,'base.html')
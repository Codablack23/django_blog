from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    myjson={
        "status":"loaded"
    }
    return render(request,'index.html')
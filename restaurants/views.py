from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

 	
def home(request):
    context = {
        "msg": "Hello World!",
    }
    return render(request, 'rest.html', context)

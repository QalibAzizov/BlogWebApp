from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.


posts = [
    {
        'author': 'CoreysMS',
        'title' : 'BlogPost 1',
        'content': 'First post content',
        'date_posted': 'November 27, 2022'
    },
    {
        'author': 'Nick Bird',
        'title' : 'BlogPost 2',
        'content': 'Second post content',
        'date_posted': 'November 29, 2022'
    }
]


def home(request):
    context = {
        'posts': posts
    }

    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html', {'title': 'About'})
    
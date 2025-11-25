from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse

# Create your views here.
def homepage(request):
    context = {
        'page': 'Home page'
    }
    return render(request, "main.html", context)

def todolist(request):
    context = {
        'page': 'Todolist page'
    }
    return render(request, "todolist.html", context)

def contact(request):
    context = {
        'page': 'Contact page'
    }
    return render(request, "contact.html", context)

def about(request):
    context = {
        'page': 'About page'
    }
    return render(request, "about.html", context)
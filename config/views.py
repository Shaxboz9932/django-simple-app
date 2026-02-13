from django.http import HttpResoponse

def index(request):
    return HttpResoponse("<h1>Hello, world!</h1>")
from django.shortcuts import render
from .models import MenuItem

def home(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'Base_App/home.html', {
        'menu_items': menu_items
    })

def menu(request):
    items = MenuItem.objects.all()   # safe, no error
    return render(request, 'Base_App/menu.html', {
        'items': items
    })

def contact(request):
    return render(request, 'Base_App/contact.html')
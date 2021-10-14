from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# /products -> index
# Uniform Resource Locator(address)


def index(request):
    products = Product.objects.all()
    # Product.objects.filter()
    # Product.objects.save()
    # Product.objects.get()
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('New product')

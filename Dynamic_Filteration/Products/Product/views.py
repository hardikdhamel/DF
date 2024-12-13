from django.shortcuts import render
from django.db.models import Q
from .models import Product

# Create your views here.

def product_list(request):
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    query_filter = Q()

    if min_price:
        query_filter &= Q(price__gte=min_price)
    if max_price:
        query_filter &= Q(price__lte=max_price)

    products = Product.objects.filter(query_filter)

    return render(request, 'product_list.html', {'products': products})

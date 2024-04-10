from django.shortcuts import render
from ecommerceapp.models import Product
from django.db.models import Q

# Create your views here.
def searchPROD(request):
    query=None
    result=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        result=Product.objects.all().filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request,'search1.html',{'query': query,'products':result})

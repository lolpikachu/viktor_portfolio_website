from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def index(request):
    return render(request, 'webapp/index_ru.html')

# def index_ru(request):
#     return render(request, 'webapp/index_ru.html')

def about(request):
    return render(request, 'webapp/about.html')

def offer(request):
    return render(request, 'webapp/services.html')    

def portfolio(request):
    return render(request, 'webapp/portfolio_ru.html')

def contact(request):
    return render(request, 'webapp/contact_ru.html')

# def services(request):
#     return render(request, 'webapp/services.html')        

def example_1(request):
    return render(request, 'webapp/portfolio/example_1.html')             

def example_2(request):
    return render(request, 'webapp/portfolio/example_2.html')    

def example_3(request):
    return render(request, 'webapp/portfolio/example_3.html')    

def example_4(request):
    return render(request, 'webapp/portfolio/example_4.html')    

def example_5(request):
    return render(request, 'webapp/portfolio/example_5.html') 

def example_6(request):
    return render(request, 'webapp/portfolio/example_6.html')    



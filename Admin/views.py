from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def add_record(request):
    return render(request, 'add_record.html')

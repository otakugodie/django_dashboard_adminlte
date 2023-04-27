from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'adminlte/index.html')

def indexDark (request):
    return render(request, 'adminlte/index2.html')
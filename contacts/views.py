from django.shortcuts import render

# Create your views here.
def contact(request):

        return render(request ,'contacts.html')

def index(request):
        return render(request, 'index.html')
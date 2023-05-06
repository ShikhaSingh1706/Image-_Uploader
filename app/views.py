from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageForm
from .models import Image



# Create your views here.
def app(request):
    return HttpResponse("hello world!")

def home(request):
    if request.method=="POST":
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form=ImageForm()
    img=Image.objects.all()
    return render(request,'home.html',{'img':img,'form':form})




from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterform
# Create your views here.
def register(request):
    if request.method=='POST':
        form= UserRegisterform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been succesfully created')
            return redirect('home')
    else:
        form= UserRegisterform()

    return render(request, 'authApp/register.html', {'form': form})

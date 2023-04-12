from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

# Create your views here.
def index(request):
    return render(request, 'chat/index.html')

def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()

    context = {
        'form': form,
    }
    return render(request, 'chat/sign_up.html', context)
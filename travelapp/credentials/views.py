from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect

# Create your views here.
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        a = request.POST['username']
        b = request.POST['first_name']
        c = request.POST['last_name']
        d = request.POST['email']
        e = request.POST['password']
        e1 = request.POST['password1']
        if e == e1:
            if User.objects.filter(username=a).exists():
                messages.info(request, "username Taken")
                return redirect('register')
            elif User.objects.filter(email=d).exists():
                messages.info(request, "email Taken")
                return redirect('register')

            else:
                user = User.objects.create_user(username=a, password=e, first_name=b, last_name=c, email=d)
            user.save()
            print("User created")
            return redirect('login')

        else:
            messages.info(request, "Password not matching")
            return redirect('/')

    return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('demo')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')

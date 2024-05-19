from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

import facturations
from facturations.models import Utilisateurs
from .forms import LoginForm


def login_page(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
    context = {'form': forms}
    return render(request, 'templatetra/login1.html', context)


def signup_page(request):
    forms = facturations.forms.UtilisateurForm()
    return render(request, 'docs/crerutilisateur.html', {'forms': forms})



def seconnecter(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user= False
            service='archive'

            try :
             user= Utilisateurs.objects.get(email=username,password=password)
            except:
                redirect('login')

            if user:
                request.session['id_user'] = user.id_utilisateur
                if user.direction=='archive' :
                    request.session["id_user"] = user.id_user
                    return render(request, 'docs/acc_archiviste.html', {'util': user,'service':service})
                else:
                    service = 'facturation'
                    request.session["id_user"] = user.id_utilisateur
                    return render(request, 'docs/dashboard.html', {'util': user})

        return redirect('login')
def deconnecter(request,id):
 return redirect('login')





def logout_page(request):
    logout(request)
    return redirect('login')

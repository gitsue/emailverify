from django.shortcuts import render, redirect
from .models import Email
import re

# Create your views here.
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
	if 'validate' not in request.session:
		request.session['validate'] = ""
	return render(request, 'verify/index.html')

def success(request):
	email = Email.objects.all()
	context = {
		"emails" : email
		}	
	if email_regex.match(request.POST['email']):
		Email.objects.create(email=request.POST['email'])
		return render(request, 'verify/success.html', context)
	else:
		request.session['validate'] = 'Email is NOT valid!'
		return redirect('/')

from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

def user_input(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            if age >= 20:
                # Save to database
                return HttpResponse("User data saved successfully!")
            else:
                return HttpResponse("Age must be 20 or above.")
    else:
        form = UserForm()
    return render(request, 'userapp/user_input.html', {'form': form})

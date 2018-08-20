from django.contrib.auth.models import User
from django import forms

class Korisnik(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','password']
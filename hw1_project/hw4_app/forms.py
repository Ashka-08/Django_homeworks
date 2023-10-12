from django import forms

from hw4_app.models import Product

class FormProductAdd(forms.Form):
    name = forms.CharField(max_length=50,
            widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Название товара'}))
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control', 
            'placeholder': 'Описание'}))
    price = forms.FloatField(min_value=0.0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Цена'}))
    prod_quant = forms.IntegerField(min_value=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Количество'}))
    img = forms.ImageField()


class FormProductsUpdate(forms.Form):
    pk = forms.ModelChoiceField(
        label='Товар', 
        empty_label='Выберите товар',
        queryset=Product.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}))
    name = forms.CharField(max_length=50,
            widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Название товара'}))
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control', 
            'placeholder': 'Описание'}))
    price = forms.FloatField(min_value=0.0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Цена'}))
    prod_quant = forms.IntegerField(min_value=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Количество'}))
    img = forms.ImageField()
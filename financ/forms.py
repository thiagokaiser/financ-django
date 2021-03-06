from django import forms
from django.forms.widgets import TextInput
from .models import Despesa, Categoria, Conta

class DespesaFormView(forms.ModelForm):    
	class Meta:
		model = Despesa
		fields = ('valor',
				  'descricao',	
				  'dt_vencimento',
				  'categoria',			
				  'pago',
				  'conta',
				)
		widgets = {
			'dt_vencimento': TextInput(attrs={'type': 'date'}),
		}

	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user', None)
		super(DespesaFormView, self).__init__(*args, **kwargs)
		if user:
			self.fields['categoria'].queryset = Categoria.objects.filter(usuario=user)
			self.fields['conta'].queryset = Conta.objects.filter(usuario=user)

class CategoriaFormView(forms.ModelForm):
	class Meta:
		model = Categoria
		fields = ('descricao',
				  'cor',
				)
		widgets = {
			'cor': TextInput(attrs={'type': 'color'}),
		}

class ContaFormView(forms.ModelForm):
	class Meta:
		model = Conta
		fields = ('descricao',)
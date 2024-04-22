from django.shortcuts import render
from medico.models import DadosMedico, Especialidades, DatasAbertas
def home(request):
    if request.method == "GET":   
        medicos = DadosMedico.objects.all() 
        especialidades = Especialidades.objects.all()
        return render(request, 'home.html',{'medicos': medicos,'especialidades':especialidades})
    
    
from django.shortcuts import render
from core.models import Evento


# Create your views here.

def lista_eventos(request):
    # usuario = request.user
    eventos = Evento.objects.all()
    context = {'eventos': eventos}
    return render(request, 'agenda.html', context)

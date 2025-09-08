from django.contrib import admin
from .models import Service

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    #  mostrar informacion de campos ocultos como solo lectura

# registrar modelos en el administrador

admin.site.register(Service, ServiceAdmin)

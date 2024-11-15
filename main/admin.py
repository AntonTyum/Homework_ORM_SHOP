from django.contrib import admin
from .models import Car, Sale, Client

admin.site.register(Client)
admin.site.register(Car)
admin.site.register(Sale)
# зарегистрируйте необходимые модели

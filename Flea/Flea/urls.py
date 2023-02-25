from django.contrib import admin
from django.urls import path

from main.views import index, contact

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
]

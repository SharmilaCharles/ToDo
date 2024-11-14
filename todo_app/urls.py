from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('addtask', views.addtask, name='addtask')
]
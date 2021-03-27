from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_home, name='home'),
    path('about', views.post_about, name='about'),
]
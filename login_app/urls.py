from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process_registration', views.process_registration),
    path('process_login', views.process_login),
    path('success/<first_name>', views.success),
]
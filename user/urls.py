from django.db import models
from django.conf.urls import url
from . import views

app_name = 'user'
urlpatterns = [
       url(r'^login/$', views.login, name='login')
]

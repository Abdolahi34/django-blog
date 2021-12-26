from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.SignUp, name='SignUp')
]

urlpatterns += staticfiles_urlpatterns()


from django.urls import path, include
from portfolio_app import views


urlpatterns = [
    path('', views.index, name='index'),
]
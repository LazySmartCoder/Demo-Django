from django.contrib import admin
from django.urls import path
from DemoWeb import views

urlpatterns = [
    path("", views.index, name = "page")
]
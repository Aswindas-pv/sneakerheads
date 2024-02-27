from django.urls import path
from sneaker_heads_app import views

urlpatterns = [
    path('', views.index_page)
]

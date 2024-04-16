from django.urls import path, include
from . import views
app_name = "customer"
urlpatterns = [
    path("", views.customer_index, name='index'),
]

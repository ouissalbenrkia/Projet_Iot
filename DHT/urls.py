from django.urls import path
from . import api

urlpatterns = [
    path("api/get", api.Dlist, name='json'),
    path("api/post", api.Dhtviews.as_view(), name='json'),
    path("dashboard/", api.dashboard, name='dashboard'),
]
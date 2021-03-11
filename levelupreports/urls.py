from django.urls import path
from .views import usergame_list
from .views import userevent_list

urlpatterns = [
    path('reports/usergames', usergame_list),
    path('reports/userevents', userevent_list),
]
from . import views
from django.urls import path
app_name = 'Search'

urlpatterns = [
    path('',views.SearchResult,name='SearchResult'),
]

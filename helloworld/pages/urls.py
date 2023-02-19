from django.urls import path
from .views import home_page_view

urlpatterns = [
    path(route='', view=home_page_view, name='home'),
]

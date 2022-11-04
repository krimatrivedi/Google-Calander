from django.urls import path
from . import views


urlpatterns = [
    path('', views.GoogleCalendarInitView, name='google_permission'),
    path('', views.GoogleCalendarRedirectView, name='google_redirect'),
   
]
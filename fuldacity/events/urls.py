from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

app_name = 'events'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]
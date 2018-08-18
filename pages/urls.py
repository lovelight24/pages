from django.conf.urls import url
from django import views as dviews
from . import views


urlpatterns = [
                url(r'^$', views.HomePageView.as_view(), name='home'),
                url(r'^about/$', views.AboutPageView.as_view(), name='about'),
                url(r'^.*$', dviews.defaults.page_not_found),
]
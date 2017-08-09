from django.conf.urls import url
from . import views

app_name = 'Music'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # /Music/2/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='Detail'),

    # /Music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # /Music/album/2/
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    # /Music/album/2/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),
]

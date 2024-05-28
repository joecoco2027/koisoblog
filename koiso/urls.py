from django.urls import path
from . import views
from users import views as users_views
urlpatterns = [
    path('', views.home, name='koiso-home'),
    path('about/', views.about, name='koiso-about'),
    path('register/', users_views.register, name='users-register'),
]

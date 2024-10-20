from django.urls import path
from .views import chat, login_view, signup_view, logout_view

urlpatterns = [
    path('', chat, name='chat'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
]

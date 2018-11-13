from django.urls import path
from .views import SettingsView, LoginView, ConnectView, OAuthCBView

urlpatterns = [
    path('settings', SettingsView.as_view()),
    path('connect', ConnectView.as_view(), name='nabmastodond.connect'),
    path('oauthcb', OAuthCBView.as_view(), name='nabmastodond.oauthcb'),
    path('login', LoginView.as_view(), name='nabmastodond.login'),
]
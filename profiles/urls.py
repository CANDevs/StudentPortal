from django.urls import path
from . import views
urlpatterns = [
    path('profile/<int:id>/',views.viewPost,name="Profile")
]

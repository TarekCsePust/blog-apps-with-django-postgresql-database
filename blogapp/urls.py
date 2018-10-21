"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .import views
from django.urls import path
app_name="blogapp"

urlpatterns = [
    path('',views.index.as_view(),name="index"),
    path('author/<name>/',views.getauthor.as_view(),name="author"),
    path('article/<id>/',views.getsingle.as_view(),name="single_post"),
    path('topic/<name>/',views.getTopic.as_view(),name="topic"),
    path('login/', views.getLogin.as_view(), name="login"),
    path('logout/', views.getLogout.as_view(), name="logout"),
    path('create/', views.getCreate.as_view(), name="create"),
    path('profile/', views.getProfile.as_view(), name="profile"),
    path('update/<int:upid>/', views.getUpdate.as_view(), name="update_post"),
    path('delete/<int:upid>/', views.getDelete.as_view(), name="delete_post"),
    path('register/', views.getRegister, name="register"),
    path('category/', views.getCategory.as_view(), name="category"),
    path('create/topic', views.createTopic.as_view(), name="create_topic"),

    path('activate/<uid>/<token>', views.activate, name="activate"),
]
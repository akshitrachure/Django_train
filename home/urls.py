from django.contrib import admin
from django.urls import path

from home.views import home_view,user_login,user_logout,register,deletestudentinfo,contact,editstudent,createstudent,about

urlpatterns = [
    path('',home_view),    
    path('login/',user_login,name="login"),
    path('logout/',user_logout,name="logout"),
    path('register/',register,name="register"),
    #path('',views.home_view)
    path('delete/<id>',deletestudentinfo),
    path('contact/',contact),
    path('about/',about),
    path('edit/<id>',editstudent),
    path('createstudent',createstudent),
]

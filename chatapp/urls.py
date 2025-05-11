from django.urls import path
from . import views
from .views import MessagesListView, InboxView

app_name = 'chatapp'

urlpatterns = [
    path('', MessagesListView.as_view(), name='message_list'),
    path('inbox/<str:username>/', InboxView.as_view(), name='inbox'),
    path('logs/', views.ActionLogListView.as_view(), name='log_list'),
    
]

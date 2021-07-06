from django.urls import path, include
from .import views
urlpatterns = [
path('todos/<int:pk>',views.TodoRetrieveUpdateDestroy.as_view()),
path('todos',views.TodoListCreate.as_view()),
path('todos/<int:pk>/complete',views.TodoComplete.as_view()),
path('todos/completed',views.TodoCompletedList.as_view()),


path('signup',views.signup),
path('login',views.login)
]
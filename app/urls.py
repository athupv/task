from django.urls import path
from .views import PostCreateView, PostReadView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', PostReadView.as_view(), name='post_read'),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
]

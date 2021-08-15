from django.urls import include, path

from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

app_name = 'api'
router = DefaultRouter()
router.register(r'v1/posts', PostViewSet, basename='posts')
router.register(r'v1/groups', GroupViewSet, basename='groups')
router.register(
    r'^v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='comments'
)

urlpatterns = [
    path('', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]

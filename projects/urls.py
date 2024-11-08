from rest_framework import routers
from .views import ProjectViewSet, TaskViewSet

router = routers.DefaultRouter()

router.register("api/projects", ProjectViewSet, "projects")
router.register("api/tasks", TaskViewSet, "tasks")
urlpatterns = router.urls

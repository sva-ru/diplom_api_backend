import os

from celery import Celery
from celery.result import AsyncResult

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'netology_pd_diplom.settings')

app = Celery('netology_pd_diplom', broker_connection_retry_on_startup=True)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child, processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()



def get_result(task_id: str) -> AsyncResult:
    return AsyncResult(task_id, app=app)
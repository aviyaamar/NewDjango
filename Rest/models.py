from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Message(models.Model):
    sender = models.ForeignKey(
        User, related_name="sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(
        User, related_name="receiver", on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


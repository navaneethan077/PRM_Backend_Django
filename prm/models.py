from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=255)
    key = models.CharField(max_length=255)
    proType = models.CharField(max_length=255)
    desc = models.CharField(max_length=1000)


# class User(models.Model):
#     firstName = models.CharField(max_length=100)
#     lastName = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100, unique=True)
#     userName = models.CharField(max_length=100, unique=True)
#     password = models.CharField(max_length=150)
#     userRole = models.CharField(max_length=25)

 
class Task(models.Model):
    taskName = models.CharField(max_length=600)
    description = models.CharField(max_length=2500, null=True)
    member = models.CharField(max_length=255)
    deadline = models.DateField()
    status = models.CharField(max_length=255, default='Todo')
    projectid = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')

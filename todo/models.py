from django.db import models
from django.contrib.auth.models import User


class List(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255)
    List = models.ForeignKey(List, on_delete=models.CASCADE)
    done = models.BooleanField(default=True)


    def __str__(self):
        return self.name

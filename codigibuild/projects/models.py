from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.fields.CharField(max_length=100)
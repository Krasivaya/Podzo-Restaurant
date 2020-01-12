from django.db import models
from django import forms


class cities(models.Model):
    name = models.CharField(max_length =32)
    img = models.ImageField(upload_to='pics')
    entity = models.IntegerField()
class resto(models.Model):
    name = models.CharField(max_length =32)
    img = models.URLField(max_length =500)
    adress = models.TextField(max_length =500)
    url = models.URLField(max_length =500)

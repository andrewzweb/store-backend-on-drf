from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField()

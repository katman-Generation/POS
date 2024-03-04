from djmoney.models.fields import MoneyField
from django.db import models

# Create your models here
class Product(models.Model):
    """this is the model for the product in our store"""
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=5)
    photo = models.ImageField(upload_to='product_image', default='prod.jpg', blank=True, null=True)
    cost = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', blank=True, null=True)
    sellingPrice = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', blank=True, null=True)
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
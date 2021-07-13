from django.conf import settings
from django.db import models
from django.utils import timezone
from django_google_maps import fields as map_fields
# Create your models here.

class Address(models.Model):
    latitude=models.DecimalField (max_digits=8, decimal_places=3,null=True,blank=True,editable = False)
    longitude=models.DecimalField (max_digits=8, decimal_places=3,null=True,blank=True,editable = False)
    full_address=models.TextField()
    street=models.TextField(null=True,blank=True,editable = False)
    city=models.TextField(null=True,blank=True,editable = False)
    house_number=models.DecimalField(max_digits=8, decimal_places=3,null=True,blank=True,editable = False)
    country=models.TextField(null=True,blank=True,editable = False)
    created_date = models.DateTimeField(default=timezone.now,editable = False),
    
    def get_all(self):
        return self.latitude
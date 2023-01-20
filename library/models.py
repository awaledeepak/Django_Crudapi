from django.db import models

# Create your models here.

class Book(models.Model): 
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100,blank=True)
    # datetime = models.DateTimeField(max_length=100,blank=True)
    
    
    
def __str__(self):
    return self.id
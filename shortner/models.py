from django.db import models

# Create your models here.


class Url(models.Model):                        #This Model to save the input urls from users that will be shortened
    link        = models.CharField(max_length=10000)
    uuid        = models.CharField(max_length=10)


    


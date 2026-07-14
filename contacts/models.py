from django.db import models


class Contact(models.Model):
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=250)
    contact_email = models.EmailField()
    urgent = models.BooleanField(null=True, blank=True)

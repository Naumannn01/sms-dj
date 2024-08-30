from django.db import models
import os
from twilio.rest import Client


# Create your models here.
class Score(models.Model):
    result=models.PositiveIntegerField()

    def __str__(self):
        return str(self.result)

    def save(self, *args, **kwargs):
     if self.result < 70 :
        account_sid = "AC8be1953ea4260209a8b58631b8b9140e"
        auth_token = "cfd31ce522c91a0e8c2cabf0ca922e89"
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body="Assalamu Alaikum Osama Bhai ",
            from_="+14125674118",
            to="+918286181906",
            )

        
        return super().save(*args,**kwargs) 
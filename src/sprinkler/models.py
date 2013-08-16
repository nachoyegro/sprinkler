# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Arduino(models.Model):

    user = models.ForeignKey(User, null=True, blank=True)
    public_ip = models.CharField(max_length=255)

    def sprinkle(self):
        pass

    def get_actual_info(self):
        '''This must get actual info from arduino and save it in the database'''
        pass

    def get_last_info(self):
        '''Should return last climate info'''
        pass

class ClimateInfo(models.Model):
    arduino = models.ForeignKey(Arduino)
    temperature = models.IntegerField()
    humidity = models.IntegerField()
    luminosity = models.IntegerField()
    date = models.DateTimeField()



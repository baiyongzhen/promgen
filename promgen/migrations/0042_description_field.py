# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-21 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promgen', '0041_sender_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]

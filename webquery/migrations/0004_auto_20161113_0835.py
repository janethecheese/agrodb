# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-13 08:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webquery', '0003_auto_20161112_0850'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='location',
            new_name='name',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-08 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20170908_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(upload_to='courses/%Y/%m', verbose_name='头像'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-20 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='created_by',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]

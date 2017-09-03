# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-14 08:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('galleries', '0002_auto_20141227_0224'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryImageExtra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_date', models.DateField(blank=True, null=True, verbose_name='\u884c\u4e8b\u65e5')),
                ('image', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='extra', to='galleries.GalleryImage')),
            ],
        ),
    ]

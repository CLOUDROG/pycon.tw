# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2019-09-14 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0017_proposedtutorialevent_registration_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsoredevent',
            name='slido_embed_link',
            field=models.URLField(blank=True, default='', verbose_name='slido embed link'),
        ),
    ]

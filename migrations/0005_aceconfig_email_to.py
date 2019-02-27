# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-15 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ace', '0004_remove_aceconfig_email_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='aceconfig',
            name='email_to',
            field=models.EmailField(default='no-reply@empresa.com', help_text='Notifica\xe7\xf5es de altera\xe7\xe3o de ramais/senhas:  - Ex: <em>fulano@empresa.com</em>.', max_length=75, verbose_name='Endere\xe7o de destinat\xe1rio.'),
        ),
    ]

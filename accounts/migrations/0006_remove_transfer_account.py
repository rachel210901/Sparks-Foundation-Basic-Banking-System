# Generated by Django 3.2.5 on 2021-09-17 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_transfer_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transfer',
            name='account',
        ),
    ]
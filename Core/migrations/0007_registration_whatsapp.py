# Generated by Django 3.2.4 on 2021-09-07 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0006_auto_20210907_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='whatsapp',
            field=models.CharField(default=232323232323, max_length=10, unique=True),
            preserve_default=False,
        ),
    ]

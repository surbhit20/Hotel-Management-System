# Generated by Django 3.2.7 on 2021-09-27 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='rooms',
            field=models.IntegerField(default=1),
        ),
    ]

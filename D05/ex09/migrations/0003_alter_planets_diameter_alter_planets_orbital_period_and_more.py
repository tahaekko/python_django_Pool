# Generated by Django 4.2.13 on 2024-07-08 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex09', '0002_alter_planets_population'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planets',
            name='diameter',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='planets',
            name='orbital_period',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='planets',
            name='rotation_period',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='planets',
            name='surface_water',
            field=models.FloatField(null=True),
        ),
    ]

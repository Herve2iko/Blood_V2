# Generated by Django 2.0.13 on 2020-07-23 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0002_auto_20200722_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donors',
            name='age',
            field=models.IntegerField(),
        ),
    ]

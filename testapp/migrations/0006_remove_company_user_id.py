# Generated by Django 3.0.8 on 2021-04-14 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_auto_20210414_1155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='user_id',
        ),
    ]
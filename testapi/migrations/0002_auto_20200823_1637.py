# Generated by Django 3.1 on 2020-08-23 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='age',
            field=models.IntegerField(),
        ),
    ]

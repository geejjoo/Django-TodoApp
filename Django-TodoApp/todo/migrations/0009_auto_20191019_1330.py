# Generated by Django 2.2 on 2019-10-19 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0008_auto_20191019_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(default='test', max_length=15),
        ),
    ]

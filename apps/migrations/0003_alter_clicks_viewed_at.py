# Generated by Django 4.1.3 on 2022-12-20 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_clicks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clicks',
            name='viewed_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]

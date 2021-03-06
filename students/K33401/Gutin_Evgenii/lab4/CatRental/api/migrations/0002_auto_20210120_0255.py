# Generated by Django 3.0.5 on 2021-01-20 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='description',
            field=models.TextField(blank=True, max_length=620),
        ),
        migrations.AddField(
            model_name='cat',
            name='pic',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='order',
            name='end_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='start_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

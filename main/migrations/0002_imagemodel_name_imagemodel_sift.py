# Generated by Django 5.0.6 on 2024-05-14 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='sift',
            field=models.TextField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.0.7 on 2021-07-19 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('woodogdata', '0007_auto_20210719_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='tag',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='tag',
            field=models.IntegerField(),
        ),
    ]

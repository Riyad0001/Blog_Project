# Generated by Django 4.0.10 on 2024-11-08 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_coment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coment',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
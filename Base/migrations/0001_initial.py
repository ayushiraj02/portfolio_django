# Generated by Django 4.2.18 on 2025-01-23 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('content', models.TextField(max_length=400)),
                ('number', models.CharField(max_length=10)),
            ],
        ),
    ]

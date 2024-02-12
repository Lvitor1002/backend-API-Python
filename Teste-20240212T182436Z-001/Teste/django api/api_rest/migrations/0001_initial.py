# Generated by Django 5.0.2 on 2024-02-12 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(default='', max_length=100, primary_key=True, serialize=False)),
                ('nome', models.CharField(default='', max_length=150)),
                ('email', models.EmailField(default='', max_length=254)),
                ('idade', models.IntegerField(default=0)),
            ],
        ),
    ]
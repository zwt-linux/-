# Generated by Django 2.2.16 on 2020-11-11 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServerInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_ip', models.CharField(max_length=20)),
                ('host_name', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('app_name', models.CharField(max_length=20)),
            ],
        ),
    ]

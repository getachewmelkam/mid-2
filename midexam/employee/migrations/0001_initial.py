# Generated by Django 4.1.4 on 2023-01-01 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=10)),
                ('job', models.CharField(default='medicine', max_length=10)),
            ],
        ),
    ]

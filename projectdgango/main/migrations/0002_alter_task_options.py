# Generated by Django 4.2.2 on 2023-06-10 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Завдання', 'verbose_name_plural': 'Усі завдання'},
        ),
    ]

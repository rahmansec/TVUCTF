# Generated by Django 5.0 on 2024-04-25 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forced_injection', '0003_rename_members_member'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='member',
            table='members',
        ),
    ]
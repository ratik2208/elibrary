# Generated by Django 4.2.2 on 2023-12-08 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("elibrary_app", "0006_alter_ebooksmodel_author"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ebooksmodel",
            name="cover",
        ),
    ]

# Generated by Django 2.0.2 on 2018-03-06 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0021_auto_20171229_1056'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name', 'first_name']},
        ),
    ]

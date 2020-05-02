# Generated by Django 2.2.9 on 2020-01-18 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20200117_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='complaint',
            name='in_progress',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='complaint',
            name='institute_name',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
# Generated by Django 5.0.4 on 2024-07-27 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0007_rename_score_drink_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='team',
            field=models.CharField(default='Unknown Team', max_length=200),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.0.5 on 2020-06-11 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_bss_set1_intangible_asset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bss_set1',
            name='intangible_asset',
            field=models.DecimalField(decimal_places=3, max_digits=15),
        ),
    ]

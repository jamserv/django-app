# Generated by Django 2.2 on 2019-05-02 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0011_auto_20190501_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moroso',
            name='balance',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='moroso',
            name='cellphone',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='moroso',
            name='month',
            field=models.BigIntegerField(),
        ),
    ]

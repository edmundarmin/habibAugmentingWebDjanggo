# Generated by Django 4.1.7 on 2023-06-14 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_alter_cartorder_price_alter_product_old_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartorder',
            name='price',
            field=models.DecimalField(decimal_places=3, default='3.000', max_digits=99999999999999),
        ),
        migrations.AlterField(
            model_name='cartorderproducts',
            name='price',
            field=models.DecimalField(decimal_places=3, default='3.000', max_digits=99999999999999),
        ),
        migrations.AlterField(
            model_name='cartorderproducts',
            name='total',
            field=models.DecimalField(decimal_places=3, default='3.000', max_digits=99999999999999),
        ),
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.DecimalField(decimal_places=3, default='5.000', max_digits=99999999999999),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=3, default='3.000', max_digits=99999999999999),
        ),
    ]

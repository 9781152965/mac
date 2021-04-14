# Generated by Django 3.1.2 on 2020-10-30 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20201029_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='marked_price',
            field=models.PositiveIntegerField(default=''),
        ),
        migrations.AddField(
            model_name='product',
            name='return_policy',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='selling_price',
            field=models.PositiveIntegerField(default=''),
        ),
        migrations.AddField(
            model_name='product',
            name='warranty',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='product2',
            name='descripton',
            field=models.TextField(default=' this product is best in all aspects in term of price '),
        ),
    ]

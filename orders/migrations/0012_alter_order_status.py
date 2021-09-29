# Generated by Django 3.2.6 on 2021-09-29 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Cancelled', 'Cancelled'), ('Accepted', 'Accepted'), ('Completed', 'Completed')], default='New', max_length=15),
        ),
    ]

# Generated by Django 4.1 on 2024-05-05 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0007_alter_favorite_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sample.item'),
        ),
    ]

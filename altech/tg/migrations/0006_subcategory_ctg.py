# Generated by Django 4.1 on 2022-09-07 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tg', '0005_remove_subcategory_ctg'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='ctg',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tg.catalog'),
        ),
    ]

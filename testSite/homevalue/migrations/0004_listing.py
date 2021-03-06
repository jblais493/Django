# Generated by Django 2.1 on 2018-08-22 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homevalue', '0003_auto_20180625_1818'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('realtor', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.FloatField()),
                ('post_date', models.DateTimeField(verbose_name='date posted')),
            ],
        ),
    ]

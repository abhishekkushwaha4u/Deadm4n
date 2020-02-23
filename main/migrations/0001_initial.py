# Generated by Django 3.0.3 on 2020-02-19 15:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('location_name', models.CharField(max_length=100)),
                ('landmark', models.CharField(max_length=500)),
                ('latitude', models.CharField(max_length=20)),
                ('longitude', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='LocationAndProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.IntegerField()),
                ('discount', models.FloatField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Location')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Product')),
            ],
        ),
        migrations.CreateModel(
            name='BestDeals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deal', models.CharField(max_length=500)),
                ('valid_from', models.DateField()),
                ('valid_till', models.DateField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Location')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Product')),
            ],
        ),
    ]
# Generated by Django 4.1.2 on 2022-10-31 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=64)),
                ('listingid', models.IntegerField()),
                ('bid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=64)),
                ('comment', models.CharField(max_length=64)),
                ('listingid', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('starting_bid', models.IntegerField()),
                ('category', models.CharField(max_length=64)),
                ('image_link', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=64)),
                ('listingid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Winner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=64)),
                ('winner', models.CharField(max_length=64)),
                ('listingid', models.IntegerField()),
                ('winprice', models.IntegerField()),
                ('title', models.CharField(max_length=64, null=True)),
            ],
        ),
    ]

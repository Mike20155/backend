# Generated by Django 3.0.6 on 2020-06-20 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='test', max_length=400)),
                ('history', models.TextField(default='test', max_length=400)),
            ],
        ),
    ]
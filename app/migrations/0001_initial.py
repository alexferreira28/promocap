# Generated by Django 4.1.6 on 2023-04-29 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('cnpj', models.CharField(max_length=18)),
                ('endereco', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=20)),
            ],
        ),
    ]

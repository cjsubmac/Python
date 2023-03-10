# Generated by Django 4.1.3 on 2022-11-24 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('apellidos', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=25)),
                ('edad', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=25)),
                ('anyo', models.PositiveIntegerField()),
                ('descripcion', models.TextField()),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cine.director')),
            ],
        ),
    ]

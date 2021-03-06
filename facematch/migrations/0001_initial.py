# Generated by Django 2.1.5 on 2019-06-02 14:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance', models.BooleanField(default=False)),
                ('date', models.DateField(default=datetime.date.today)),
                ('lecture', models.SmallIntegerField()),
                ('subject', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=100)),
                ('program', models.CharField(max_length=50)),
                ('semester', models.PositiveIntegerField()),
                ('section', models.CharField(max_length=2)),
                ('image', models.ImageField(upload_to='students_pics')),
            ],
        ),
        migrations.CreateModel(
            name='TempFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='raw_files')),
            ],
        ),
        migrations.AddField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='facematch.Student'),
        ),
    ]

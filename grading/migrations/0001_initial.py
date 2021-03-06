# Generated by Django 3.1 on 2020-09-09 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('draftapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Semester', models.IntegerField(default=1)),
                ('Math_Grade', models.FloatField(default=0.0)),
                ('Physics_Grade', models.FloatField(default=0.0)),
                ('Chemistry_Grade', models.FloatField(default=0.0)),
                ('English_Grade', models.FloatField(default=0.0)),
                ('Arabic_Grade', models.FloatField(default=0.0)),
                ('History_Grade', models.FloatField(default=0.0)),
                ('Geography_Grade', models.FloatField(default=0.0)),
                ('Tarbiya_Grade', models.FloatField(default=0.0)),
                ('Average', models.FloatField(default=0.0)),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='draftapp.student')),
            ],
            options={
                'unique_together': {('Student', 'Semester')},
            },
        ),
    ]

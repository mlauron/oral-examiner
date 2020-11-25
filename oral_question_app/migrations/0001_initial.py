# Generated by Django 2.2.8 on 2020-11-23 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avatars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatarname', models.CharField(max_length=122)),
                ('file', models.FileField(upload_to='avatars/')),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=122)),
                ('file', models.FileField(upload_to='questions/')),
            ],
        ),
        migrations.CreateModel(
            name='Voices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voicename', models.CharField(max_length=122)),
                ('file', models.FileField(upload_to='voices/')),
            ],
        ),
    ]

# Generated by Django 3.2 on 2022-11-22 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signlanguage', '0007_delete_aimodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='AiModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.FileField(upload_to='')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
            ],
        ),
    ]

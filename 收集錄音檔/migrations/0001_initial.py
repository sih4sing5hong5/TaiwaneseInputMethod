# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-20 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='語料表',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('收錄時間', models.DateField(auto_now_add=True)),
                ('上尾修改時間', models.DateField(auto_now=True)),
                ('漢字', models.TextField(blank=True)),
                ('臺羅', models.TextField(blank=True)),
                ('音檔', models.FileField(blank=True, upload_to='')),
                ('備註', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]

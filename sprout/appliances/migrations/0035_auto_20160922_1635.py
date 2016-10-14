# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-22 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appliances', '0034_provider_allow_renaming'),
    ]

    operations = [
        migrations.AddField(
            model_name='appliancepool',
            name='is_container',
            field=models.BooleanField(
                default=False, help_text=b'Whether the pool uses containers.'),
        ),
        migrations.AddField(
            model_name='group',
            name='templates_url',
            field=models.TextField(
                blank=True, help_text=b'Location of templates. Currently used for containers.',
                null=True),
        ),
        migrations.AddField(
            model_name='provider',
            name='container_base_template',
            field=models.CharField(
                blank=True, help_text=b'Base tempalte for containerized ManageIQ deployment.',
                max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='template',
            name='container',
            field=models.CharField(
                blank=True,
                help_text=(
                    b'Whether the appliance is located in a container in the VM. '
                    b'This then specifies the container name.'),
                max_length=32,
                null=True),
        ),
    ]
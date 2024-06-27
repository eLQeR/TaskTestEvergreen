# Generated by Django 5.0.6 on 2024-06-27 11:32

import image_cropping.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_task', '0002_alter_page_header'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '430x360', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
    ]

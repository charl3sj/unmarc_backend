# Generated by Django 2.2.5 on 2019-11-10 17:17
from django.contrib.auth.models import Permission, Group
from django.db import migrations

from ..constants import (
    apps_excluded_from_library_admin_group as excluded_app_labels,
    library_admin_group_name
)


def assign_valid_permissions_to_library_admin_group(apps, schema_editor):
    lib_admin_grp = Group.objects.get(name=library_admin_group_name)
    perms_to_assign = Permission.objects.exclude(content_type__app_label__in=excluded_app_labels)
    lib_admin_grp.permissions.set(list(perms_to_assign))


def reverse_func(apps, schema_editor):
    lib_admin_grp = Group.objects.get(name=library_admin_group_name)
    lib_admin_grp.permissions.clear()


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191110_1626'),
    ]

    operations = [
        migrations.RunPython(assign_valid_permissions_to_library_admin_group, reverse_func),
    ]

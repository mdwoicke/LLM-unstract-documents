# Generated by Django 4.2.1 on 2023-09-20 12:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tenant_account", "0003_alter_organizationmember_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="organizationmember",
            name="member_id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]

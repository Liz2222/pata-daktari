# Generated by Django 4.0.5 on 2022-07-13 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_labtest_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientappointment',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
    ]

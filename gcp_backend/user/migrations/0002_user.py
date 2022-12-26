# Generated by Django 4.1.4 on 2022-12-20 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('org_mail', models.CharField(blank=True, max_length=100, null=True)),
                ('ph_num', models.CharField(blank=True, max_length=13, null=True)),
                ('password', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('role', models.CharField(choices=[('admin', '0'), ('student', '2'), ('club_admin', '1')], default='student', max_length=50)),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.organization')),
            ],
        ),
    ]
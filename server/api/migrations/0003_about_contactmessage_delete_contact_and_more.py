# Generated by Django 5.1 on 2024-08-10 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_contact_service_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='about/')),
                ('resume', models.FileField(upload_to='resume/')),
            ],
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='link',
            new_name='code_link',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='project',
            name='live_link',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]

# Generated by Django 4.1.7 on 2023-05-02 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0004_curso_aprenderas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='name',
            new_name='nombre',
        ),
    ]

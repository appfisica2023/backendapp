# Generated by Django 4.2.3 on 2023-07-13 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MedicamentoVitamina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tipo', models.CharField(choices=[('medicamento', 'Medicamento'), ('vitamina', 'Vitamina')], max_length=20)),
                ('hora_ingesta', models.TimeField()),
                ('realizado', models.BooleanField(default=False)),
            ],
        ),
    ]

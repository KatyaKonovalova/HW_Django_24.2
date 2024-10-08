# Generated by Django 5.0.7 on 2024-08-07 15:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0003_alter_lesson_link_to_video"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "payments_date",
                    models.DateTimeField(auto_now=True, verbose_name="дата оплаты"),
                ),
                (
                    "payment_sum",
                    models.PositiveIntegerField(verbose_name="сумма платежа"),
                ),
                (
                    "payment_method",
                    models.CharField(
                        choices=[("cash", "наличные"), ("card", "банковский перевод")],
                        default="card",
                        max_length=50,
                        verbose_name="способ оплаты",
                    ),
                ),
                (
                    "payment_link",
                    models.URLField(
                        blank=True,
                        max_length=400,
                        null=True,
                        verbose_name="ссылка на оплату",
                    ),
                ),
                (
                    "payment_id",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="идентификатор платежа",
                    ),
                ),
                (
                    "paid_course",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="courses.course",
                        verbose_name="оплаченный курс",
                    ),
                ),
                (
                    "paid_lesson",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="courses.lesson",
                        verbose_name="оплаченный урок",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Платеж",
                "verbose_name_plural": "Платежи",
                "ordering": ["-payments_date"],
            },
        ),
    ]

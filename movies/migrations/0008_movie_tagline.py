# Generated by Django 4.2.5 on 2023-11-12 13:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0007_movie_tmdb_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="tagline",
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
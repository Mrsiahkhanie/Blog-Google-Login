# Generated by Django 3.1.4 on 2021-06-03 08:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('SlideShow', '0002_auto_20210603_0134'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-publish'], 'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
        migrations.AlterModelOptions(
            name='slideshow',
            options={'ordering': ['-article__publish'], 'verbose_name': 'Slide Show', 'verbose_name_plural': 'Slide Shows'},
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='images', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='article',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='publish'),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.BooleanField(default=False, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_en',
            field=models.CharField(max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_fa',
            field=models.CharField(max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='slideshow',
            name='article',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='SlideShow.article', verbose_name='Article'),
        ),
        migrations.AlterField(
            model_name='slideshow',
            name='status',
            field=models.BooleanField(default=False, verbose_name='status'),
        ),
    ]
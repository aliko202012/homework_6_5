from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=155)
    birdthdate= models.DateField()

    def __str__ (self):
        return self.name
    class Meta:
        verbose_name ='Автор'
        verbose_name_plural='авторы'

class Book(models.Model):
    title = models.CharField(max_length=155)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')


    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class Genre(models.Model):
    name = models.CharField(max_length=155)
    books = models.ManyToManyField('Book', related_name='genres')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
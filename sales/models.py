from django.db import models
from books.models import Book

# Create your models here.
class Sale (models.Model):
  book = models.ForeignKey(Book, on_delete=models.CASCADE, default=None)
  quantity = models.PositiveIntegerField()
  price = models.FloatField()
  date_created = models.DateTimeField(auto_now_add=True)
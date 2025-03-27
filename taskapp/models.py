from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Board(models.Model):
    name =models.CharField(max_length=100)
    description=models.TextField(blank=True,null=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='boards')
    created_at=models.DateTimeField(default=timezone.now)
    members=models.ManyToManyField(User,related_name='shared_boards')
    def __str__(self):
        return self.name


class Column(models.Model):
    board= models.ForeignKey(Board,on_delete=models.CASCADE,related_name='columns')
    name =models.CharField(max_length=100)
    order=models.PositiveIntegerField(default=0)
    color=models.CharField(max_length=20,default='#FFFFFF')

    class meta:
        ordering =[ 'order']
    def __str__(self):
        return f"{self.board.name} -{self.name}"
    
    
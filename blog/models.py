from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Games(models.Model):
    game = models.CharField(max_length=128)

    def __str__(self):
        return self.game

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    postname = models.CharField(max_length=128) # 업적명
    contents = models.TextField() # 한줄평
    
    mainphoto = models.ImageField(null = True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now()) #작성시간

    disclosure = models.BooleanField(default=False) # 기본적으로는 비공개
    modified = models.DateTimeField(default=timezone.now()) # 공개날짜

    game = models.ManyToManyField(Games)
    
    def __str__(self):
        return self.postname
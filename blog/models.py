from django.db import models
from datetime import date


class Post(models.Model):
    post_title = models.CharField(max_length=250)
    post_date = models.DateField(default=date.today())
    post_content = models.TextField()

    def __str__(self):
        return self.post_title

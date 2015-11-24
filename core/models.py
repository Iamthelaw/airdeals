from django.db import models


class Post(models.Model):
    '''Db model for blog posts
    '''
    header = models.CharField(max_length=150)
    text = models.TextField()
    image = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.header


class Deal(models.Model):
    '''Main model for special deals
    '''
    header = models.CharField(max_length=150)
    description = models.TextField()
    image = models.CharField(max_length=150, null=True, blank=True)
    link = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.header

from django.db import models

# Create your models here.
class Course(models.Model):
	name = models.CharField(max_length = 250)
	language = models.CharField(max_length = 100)
	price = models.DecimalField(max_digits = 21, decimal_places = 2)
	
	def __str__(self):
		return self.name
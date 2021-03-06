from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Asset(models.Model):

	CATEGORY_CHOICE=(
		('EC', 'Electronics'),
		('FRN', 'Furnitures'),
		('BOOK', 'Book'),

		)

	# author = models.ForeignKey(User, on_delete=models.CASCADE)
	item = models.CharField(max_length=200)
	serial = models.CharField(max_length=25)
	category = models.CharField(max_length=35, choices=CATEGORY_CHOICE)
	# Creation and last modifications dates
	created_date = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	value = models.DecimalField(max_digits=19, decimal_places=2,)
	number = models.PositiveIntegerField( default=1)
	acquisition_date = models.DateField()

    
    
	# def __str__(self):
	# 	return self.name

	def publish(self):
		self.published_date = timezone.now()
		self.save()
	    
	def __str__(self):
		return self.item
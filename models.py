from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


closed_choices = (
    ('U', 'Unknown'),
    ('O', 'Open'),
    ('C', 'Closed'),
)
day_choices = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')


# Create your models here.
class Brewery(models.Model):
    brewery_name = models.CharField(max_length=200)
    notes = models.CharField(max_length=250, default="", blank=True)
    address_line1 = models.CharField("Address line 1", max_length = 50, blank=True)
    city = models.CharField(max_length = 50, blank = True)
    state = models.CharField("State (abbreviation)", max_length = 2, blank = True)
    zip_code = models.CharField("Zip Code", max_length = 10, blank=True)
    price_today= models.CharField(blank=True, max_length=6)
    #full_address = models.CharField(max_length= 250, blank=True)
    #coordinates = models.CharField(max_length = 100, blank=True)
    website = models.CharField(max_length = 100, blank = True)
    search_tags = models.CharField(max_length = 250, blank = True)
    def __unicode__(self): #this names each object as the brewery name instead of the default "Brewery object"
        return self.brewery_name

class Prices(models.Model):
    brewery = models.ForeignKey(Brewery)
    monday = models.DecimalField(max_digits=4, validators=[MinValueValidator(0)], decimal_places=2, null = True)
    tuesday = models.DecimalField(max_digits=4, validators=[MinValueValidator(0)], decimal_places=2, null = True)
    wednesday = models.DecimalField(max_digits=4, validators=[MinValueValidator(0)], decimal_places=2, null = True)
    thursday = models.DecimalField(max_digits=4, validators=[MinValueValidator(0)], decimal_places=2, null = True)
    friday = models.DecimalField(max_digits=4, validators=[MinValueValidator(0)], decimal_places=2, null = True)
    saturday = models.DecimalField(max_digits=4, validators=[MinValueValidator(0)], decimal_places=2, null = True)
    sunday = models.DecimalField(max_digits=4, validators=[MinValueValidator(0)], decimal_places=2, null = True)
    brewery_confirmed = models.BooleanField(default=False)
 
class User_added_deal(models.Model):
    brewery = models.ForeignKey(Brewery)
    Sunday = models.DecimalField(max_digits=4, validators=[MinValueValidator(0), MaxValueValidator(100)], decimal_places=2, null = True)
    Monday = models.DecimalField(max_digits=4, validators=[MinValueValidator(0), MaxValueValidator(100)], decimal_places=2, null = True)
    Tuesday = models.DecimalField(max_digits=4, validators=[MinValueValidator(0), MaxValueValidator(100)], decimal_places=2, null = True)
    Wednesday = models.DecimalField(max_digits=4, validators=[MinValueValidator(0), MaxValueValidator(100)], decimal_places=2, null = True)
    Thursday = models.DecimalField(max_digits=4, validators=[MinValueValidator(0), MaxValueValidator(100)], decimal_places=2, null = True)
    Friday = models.DecimalField(max_digits=4, validators=[MinValueValidator(0), MaxValueValidator(100)], decimal_places=2, null = True)
    Saturday = models.DecimalField(max_digits=4, validators=[MinValueValidator(0), MaxValueValidator(100)], decimal_places=2, null = True)
    TimeSubmitted = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(default=1)
    submitted_ip = models.GenericIPAddressField(null=True)
    def change_to_closed(deal):
        if deal.Sunday == 0:
            deal.Sunday="closed"
        if deal.Monday==0:
            deal.Monday="closed"
        if deal.Tuesday==0:
            deal.Tuesday="closed"
        if deal.Wednesday==0:
            deal.Wednesday="closed"
        if deal.Thursday==0:
            deal.Thursday="closed"
        if deal.Friday==0:
            deal.Friday="closed"
        if deal.Saturday==0:
            deal.Saturday="closed"


class Displayed_prices(models.Model):
    brewery = models.OneToOneField(Brewery)
    Sunday = models.CharField(max_length=12)
    Monday = models.CharField(max_length=12)
    Tuesday = models.CharField(max_length=12)
    Wednesday = models.CharField(max_length=12)
    Thursday = models.CharField(max_length=12)
    Friday = models.CharField(max_length=12)
    Saturday = models.CharField(max_length=12)
    last_modified = models.DateTimeField(auto_now=True)
    brewery_confirmed = models.BooleanField(default=False)
    def change_to_closed(deal):
        if deal.Sunday == 0:
            deal.Sunday="closed"
        if deal.Monday==0:
            deal.Monday="closed"
        if deal.Tuesday==0:
            deal.Tuesday="closed"
        if deal.Wednesday==0:
            deal.Wednesday="closed"
        if deal.Thursday==0:
            deal.Thursday="closed"
        if deal.Friday==0:
            deal.Friday="closed"
        if deal.Saturday==0:
            deal.Saturday="closed"
    #def __str__(self):
        #return '%s prices' % (brewery)







class Graveyard_submissions(models.Model):
    brewery = models.ForeignKey(Brewery)
    Sunday = models.DecimalField(max_digits=4, validators=[MinValueValidator(0), MaxValueValidator(100)], decimal_places=2, null = True)
    Monday = models.DecimalField(max_digits=4, validators=[MinValueValidator(0), MaxValueValidator(100)], decimal_places=2, null = True)
    Tuesday = models.DecimalField(max_digits=4, validators=[MinValueValidator(0), MaxValueValidator(100)], decimal_places=2, null = True)
    Wednesday = models.DecimalField(max_digits=4, validators=[MinValueValidator(0), MaxValueValidator(100)], decimal_places=2, null = True)
    Thursday = models.DecimalField(max_digits=4, validators=[MinValueValidator(0), MaxValueValidator(100)], decimal_places=2, null = True)
    Friday = models.DecimalField(max_digits=4, validators=[MinValueValidator(0), MaxValueValidator(100)], decimal_places=2, null = True)
    Saturday = models.DecimalField(max_digits=4, validators=[MinValueValidator(0), MaxValueValidator(100)], decimal_places=2, null = True)
    TimeSubmitted = models.DateTimeField(auto_now_add=True)
    submitted_ip = models.GenericIPAddressField(null=True)




class user_added_brewery(models.Model):
    brewery_name =  models.CharField(max_length=200)
    website = models.CharField(max_length = 100, blank = True)
    address_line1 = models.CharField("Address line 1", max_length = 50, blank=True)
    city = models.CharField(max_length = 50, blank = True)
    state = models.CharField("State (abbreviation)", max_length = 2, blank = True)
    zip_code = models.CharField("Zip Code", max_length = 10, blank=True)
    time_submitted = models.DateTimeField(auto_now_add=True)
    submitted_ip = models.GenericIPAddressField(null=True)

class site_header_set(models.Model):
    header_set_name = models.CharField(max_length=25, default="default")
    Monday_line_1 = models.CharField(max_length=50, blank=True)
    Monday_line_2 = models.CharField(max_length=50, blank=True)
    Tuesday_line_1 = models.CharField(max_length=50, blank=True)
    Tuesday_line_2 = models.CharField(max_length=50, blank=True)
    Wednesday_line_1 = models.CharField(max_length=50, blank=True)
    Wednesday_line_2 = models.CharField(max_length=50, blank=True)
    Thursday_line_1 = models.CharField(max_length=50, blank=True)
    Thursday_line_2 = models.CharField(max_length=50, blank=True)
    Friday_line_1 = models.CharField(max_length=50, blank=True)
    Friday_line_2 = models.CharField(max_length=50, blank=True)
    Saturday_line_1 = models.CharField(max_length=50, blank=True)
    Saturday_line_2 = models.CharField(max_length=50, blank=True)
    Sunday_line_1 = models.CharField(max_length=50, blank=True)
    Sunday_line_2 = models.CharField(max_length=50, blank=True)
    def __unicode__(self): 
        return self.header_set_name

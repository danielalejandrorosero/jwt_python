from django.db import models



class Product(models.Model):

    sku = models.CharField(max_length=100,help_text="Enter stock keeping unit")
    name = models.CharField(max_length=200,help_text="Enter product name")
    description = models.TextField(help_text="Enter product description")


    buyPrice = models.DecimalField(decimal_places=2, max_digits=20,help_text="Enter product price per unit")
    sellPrice = models.DecimalField(decimal_places=2, max_digits=20,help_text="Enter product price per unit")

    unit = models.CharField(max_length=10,help_text="ENTER TO PRODUCT")
    quantity = models.DecimalField(decimal_places=1, max_digits=20,help_text="Enter quantity")

    def get_absolute_url(self):

         return reverse('product-detail-view', args=[str(self.id)])
    
    def __str__(self):
        
        return self.sku
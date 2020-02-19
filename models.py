from django.db import models
# Create your models here.
class Category(models.Model):
    Cname=models.CharField( primary_key=True,unique=True,max_length=50) 
    class Meta:
        db_table='Category'
    def __str__(self):
        return self.Cname
    def __str__(self):
        return self.Cname

class User(models.Model):
    Name = models.CharField(max_length=30)
    Contact = models.CharField(max_length=15)
    Email = models.EmailField(primary_key=True, max_length=255)
    Password = models.CharField(max_length=16)
    Dp=models.ImageField(upload_to='images/',null=True,blank=True)
    class Meta:
        db_table='user'
    def __str__(self):
        return self.Name

class Product(models.Model):
    Name=models.CharField(max_length=50)
    Price=models.FloatField()
    Discounted_price=models.FloatField()
    descriptions=models.TextField()
    Cname=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    Image=models.ImageField(upload_to='images/',default='')
    class Meta:
        db_table='Product'
    def __str__(self):
        return self.Name

class Cart(models.Model):
    Product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, blank=True)
    Email = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # active = models.BooleanField(default=True)
    Quantity = models.IntegerField(default=1)

    class Meta:
        db_table = 'cart'
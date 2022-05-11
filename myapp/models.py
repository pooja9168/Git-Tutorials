from django.db import models



class  User(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=250)
    desgination=models.CharField(max_length=150)
    email=models.CharField(max_length=230)
    contact=models.CharField(max_length=250)


    def __str__(self):
        return self.name


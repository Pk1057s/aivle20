from django.db import models

class UploadedImage(models.Model):
    image=models.ImageField(upload_to='uploaded_images/')
    uploaded_at=models.DateTimeField(auto_now_add=True)
    
# Create your models here.

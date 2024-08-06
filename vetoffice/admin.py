from django.contrib import admin

# Register your models here.
from .models import Owner, Patient

# Register your models here.
admin.site.register(Owner)
admin.site.register(Patient)
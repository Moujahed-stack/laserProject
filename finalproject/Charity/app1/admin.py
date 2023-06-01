from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Donation)

admin.site.register(Content)
admin.site.register(Program)
admin.site.register(Profile)

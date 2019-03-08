from django.contrib import admin
from .models import Listing

# Adding features in admin site
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('price', 'realtor')
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'city')
    list_per_page = 25

# Register Listing in the admin site
admin.site.register(Listing, ListingAdmin)
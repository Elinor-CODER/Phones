from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path

import phones
from phones.views import show_product, show_catalog, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', phones.views.index),
    path('catalog/', show_catalog, name='show_catalog'),
    path('catalog/<slug:slug>/', show_product, name='show_product'),
]

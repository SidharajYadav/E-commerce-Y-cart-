from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopNow"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="Contact Us"),
    path("tracker/", views.tracker, name="Tracking Status"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
    ]

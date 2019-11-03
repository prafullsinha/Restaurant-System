from django.urls import path, include
from django.conf import settings
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from .models import Restaurant, Dish
from .forms import RestaurantForm, DishForm
from .views import RestaurantCreate, DishCreate, RestaurantDetail, review
from django.conf.urls.static import static

urlpatterns = [
    path('', ListView.as_view(queryset=Restaurant.objects.filter(date__lte=timezone.now()).order_by('date')[:5],
                              context_object_name='latest_restaurant_list',
                              template_name='myrestaurants/restaurant_list.html'), name='restaurant_list'),
    path('restaurants/<int:pk>/', RestaurantDetail.as_view(), name='restaurant_detail'),
    path('restaurants/<int:pk>/dishes/<int:pk>/', DetailView.as_view(model=Dish, template_name='myrestaurants'
                                                                                               '/dish_detail.html'),
         name='dish_detail'),
    path('restaurants/create/', RestaurantCreate.as_view(), name='restaurant_create'),
    path('restaurants/edit/',
         UpdateView.as_view(model=Restaurant, template_name='myrestaurants/form.html', form_class=RestaurantForm),
         name='restaurant_edit'),
    path('restaurants/<int:pk>/dishes/create/', DishCreate.as_view(), name='dish_create'),
    path('restaurants/<int:pk>/dishes/edit/', UpdateView.as_view(model=Dish, template_name='myrestaurants/form'
                                                                                           '.html', form_class=
                                                                 DishForm), name='dish_edit'),
    path('restaurants/<int:pk>/reviews/create/', review, name='review_create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

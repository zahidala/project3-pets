from django.urls import path
from . import views

urlpatterns = [
    #R outes in express , urls in django
    path('', views.home , name='home'),
    path('services/<int:service_id>', views.services_detail, name='detail'),
    path('appointments/create', views.AppointmentsCreate.as_view(), name='appointments_create'),
    path('myAppointments/' , views.my_appointments , name='my_appointments'),
    path('appointments/<int:pk>/delete' , views.AppointmentsDelete.as_view(), name='appointments_delete'),
    path('pets/create/' , views.PetsCreate.as_view() , name='pets_create'),
    path('appointments/<int:appointment_id>' , views.appointments_detail , name='appointments_detail'),

]
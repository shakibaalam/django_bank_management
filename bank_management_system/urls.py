from django.contrib import admin
from django.urls import path, include
from main.views import HomeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('transactions/', include('transactions.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

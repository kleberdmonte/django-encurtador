from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('urlapp.urls', namespace='urlapp')),
    # url('^short/', include('shorturls.urls'))
    # url(r'^weeny/', include("weeny.urls")),
]
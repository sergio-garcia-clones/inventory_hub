from django.conf.urls.defaults import *
 
urlpatterns = patterns('quotations.views',
    url(r'^$', 'index', name='index'),
    url(r'customer/$', 'customer', name='customer'),
    url(r'create/(?P<customer_id>\d+)/$', 'create', name='create'),
    url(r'delete/$', 'delete', name='delete'),
    url(r'invoice/(?P<quotation_id>\d+)/$', 'invoice', name='invoice'),
    url(r'update/(?P<quotation_id>\d+)/$', 'update', name='update'),
)

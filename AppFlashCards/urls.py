from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('createcard/',views.createcard,name='createcard'),
    path('createcard/addcard/',views.addcard,name='addcard'),
    path('show/<int:id>/',views.show,name='show'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('memorize/',views.memorize,name='memorize'),
    path('?',views.search,name='search'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('updatecard/<int:id>',views.updatecard,name='updatecard')
]
handler404 = 'AppFlashCards.views.handler404'

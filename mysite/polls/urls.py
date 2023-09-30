from django.urls import path

from . import views

app_name='polls'
urlpatterns=[
    # ex: /polls/
    path('', view=views.IndexView.as_view(), name='index'),
    path('',  name='index',view=views.IndexView.as_view(),),
    # ex: /polls/5/
    path('<int:pk>/',views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/',views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/',views.vote, name='vote'),

]
from django.shortcuts import render

from Insta2.models import Post
# Create your views here.

from django.views.generic import TemplateView, ListView, DetailView

class HelloWorld(TemplateView):
    template_name = 'test.html'

class PostsView(ListView):
    model = Post
    template_name = 'index.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
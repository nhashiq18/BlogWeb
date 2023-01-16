from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

#dummy post

# Create your views here.
def homepage(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
class PostDetailView(DetailView):
    model = Post

def about(request):
    return render(request, 'blog/about.html', {'title': 'about'}) 


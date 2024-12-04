from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import DetailView
from .models import Post

# Create your views here.


def posts_list(request):
    posts = Post.objects.all()

    # Получаем количество статей на странице из GET-параметров, по умолчанию 5
    posts_per_page = request.GET.get('posts_per_page', 5)

    paginator = Paginator(posts, posts_per_page)  # Создаем пагинатор
    page_number = request.GET.get('page')  # Получаем номер страницы из GET-параметров
    page_obj = paginator.get_page(page_number)  # Получаем объекты для текущей страницы

    return render(request, 'post_list.html', {'page_obj': page_obj, 'posts_per_page': posts_per_page})


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post_detail.html'

from django.shortcuts import render
from ice_cream.models import IceCream


def index(request):
    template = 'homepage/index.html'

    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'price', 'description'
    ).filter(
        is_published=True,  # Сорт разрешён к публикации;
        is_on_main=True,  # Сорт разрешён к публикации на главной странице;
        category__is_published=True  # Категория разрешена к публикации.
    )

    return render(request, template, {'ice_cream_list': ice_cream_list})

from django.shortcuts import render
from .models import Topic
from django.db.models import Q

def home(request):
    search = request.GET.get('search', '')

    if search:
        all_topics = Topic.objects.all()
        search_terms = search.split(' ')
        filtered_set = set()

        for term in search_terms:
            if term:
                filtered_set.update(all_topics.filter(Q(title__icontains=term) | Q(content__icontains=term)))

        filtered_list = list(filtered_set)
    else:
        search = ""
        filtered_list = Topic.objects.all()

    context = {
        'search': search,
        'title': 'Home',
        'topics': filtered_list,
    }

    return render(request, 'core/home.html', context)

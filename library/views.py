from django.shortcuts import render
from .models import Book


def book_list(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'library/book_list.html', context)

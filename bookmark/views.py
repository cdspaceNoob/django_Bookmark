from django.shortcuts import render

# 목록을 보여주는 뷰 만들기
from django.views.generic.list import ListView
from .models import Bookmark

# 북마크 추가 기능 구현을 위한 임포트 + 북마크 수정 기능 구현을 위한 임포트
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# 북마크 확인 기능 구현을 위한 임포트
from django.views.generic.detail import DetailView

# Create your views here.
# 목록을 보여주는 뷰 만들기
class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 6

# 북마크 추가 기능 구현을 위한 코드
class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

# 북마크 확인 기능 구현을 위한 코드
class BookmarkDetailView(DetailView):
    model = Bookmark

# 북마크 수정 기능 구현을 위한 코드
class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')

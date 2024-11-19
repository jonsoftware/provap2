from django.shortcuts import render
from django.views.generic import ListView,CreateView
from todos.models import Todo
from django.urls import reverse_lazy
class Todolistview(ListView):
    model = Todo
    templade_name = "todos/todo_list.html"


class TodoCreateView(CreateView):
    model=Todo
    fields=["title","deadline","finished_at"]
    templades_name = "todos/todo_form.html"
    success_url = reverse_lazy("todo_list")
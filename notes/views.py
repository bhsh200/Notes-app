from django.shortcuts import render

tasks=["foo", "bar", "baz"]

def index(request):
    return render(request, "notes/index.html", {
        "tasks":tasks
    })
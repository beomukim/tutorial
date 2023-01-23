from django.shortcuts import render
from community.forms import *
# Create your views here.
def write(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = Form()

    return render(request, 'write.html', {'form':form})

def list(reqeust):
    articleList = Article.objects.all()
    return render(reqeust, 'list.html', {'articleList':articleList})

def view(request, num):
    article = Article.objects.get(id=num)
    return render(request, 'view.html', {'article':article})
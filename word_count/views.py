from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request,'home.html',{'abhiram':'1233'})
def about(request):
    return render(request,'about.html')
def count(request):
    count_text=request.GET['count-text']
    c=count_text.split()
    count=len(c)
    word_dict={}
    for word in c:
        if word in word_dict:
            word_dict[word] += 1
        else :
            word_dict[word]=1
    word_dict=sorted(word_dict.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'count_text_dict':word_dict,'word_count':count})
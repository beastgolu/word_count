from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, "home.html")


def wcount(request):
    inp = request.GET["flex"]
    full = inp.split()
    dict1 = {}
    for i in full:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    ert = sorted(dict1.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, "index.html", {"text_1": full, "dict2": ert})

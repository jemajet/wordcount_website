from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, "home.html")


def count(request):
    fulltext = request.GET["fulltext"]
    wordlist = fulltext.split()

    freqdictionary = freqdict(wordlist)
    sorted_words = sorted(freqdictionary.items(),
                          key=lambda x: x[1], reverse=True)

    return render(request, "count.html", {"fulltext": fulltext,
                                          "count": len(wordlist),
                                          "sorted_words": sorted_words})


def freqdict(wordlist):
    worddict = {}
    for word in wordlist:
        if word in worddict:
            # increase
            worddict[word] += 1
        else:
            # add to dict with freq 1
            worddict[word] = 1

    return worddict


def about(request):
    return render(request, "about.html")

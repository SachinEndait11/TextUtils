# I have created this file - Sachin
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("<h1>Sachin</h1>")

def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcap = request.POST.get('fullcaps','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    newlineremover = request.POST.get('newlineremover','off')
    analyzed = djtext
    if(removepunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
    if(fullcap == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char.upper()

        params = {'purpose': 'Extra space remover', 'analyzed_text': analyzed}
        djtext = analyzed
    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Extra space remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if(removepunc != "on" and fullcap != "on" and extraspaceremover != "on" and newlineremover != "on"):
        return HttpResponse('Error')

    return render(request, "analyze.html", params)
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def testpaper(request):
    que="Who Developed Python?"
    a="Dennis Ritchie"
    b="Guido Van Rossum"
    c="Ken Thompson"
    d="Bjarne Stroustrup"
    context={
        'que':que,
        'options':[a,b,c,d]
        
    }
    template=loader.get_template('testpaper.html')
    res=template.render(context,request)
    return HttpResponse(res)

def result(request):
    s="<h1>This is your Result</h1>"
    return HttpResponse(s)
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def homepage(request):
    template=loader.get_template('homepage.html')
    return HttpResponse(template.render())
def first(request):
    template=loader.get_template('first.html')
    return HttpResponse(template.render())
def english_songs(request):
    template=loader.get_template('english_songs.html')
    return HttpResponse(template.render())
def shape_of_you(request):
    template=loader.get_template('shape_of_you.html')
    return HttpResponse(template.render())
def dandelions(request):
    template=loader.get_template('dandelions.html')
    return HttpResponse(template.render())
def believer(request):
    template=loader.get_template('believer.html')
    return HttpResponse(template.render())
def perfect(request):
    template=loader.get_template('perfect.html')
    return HttpResponse(template.render())
def love_me_like_you_do(request):
    template=loader.get_template('love_me_like_you_do.html')
    return HttpResponse(template.render())
def tamil_songs(request):
    template=loader.get_template('tamil_songs.html')
    return HttpResponse(template.render())
def hukum(request):
    template=loader.get_template('hukum.html')
    return HttpResponse(template.render())
def nira(request):
    template=loader.get_template('nira.html')
    return HttpResponse(template.render())
def naa_ready(request):
    template=loader.get_template('naa_ready.html')
    return HttpResponse(template.render())
def naan_gaali(request):
    template=loader.get_template('naan_gaali.html')
    return HttpResponse(template.render())
def aval(request):
    template=loader.get_template('aval.html')
    return HttpResponse(template.render())
def login(request):
    template=loader.get_template('login.html')
    return HttpResponse(template.render())
def signup(request):
    template=loader.get_template('signup.html')
    return HttpResponse(template.render())
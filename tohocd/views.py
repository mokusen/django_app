from django.shortcuts import render, redirect
from .forms import FindForm, DetailForm
from .services import songService, circleService, cdService, vocalService, lyricService, arrangeService, orisongService, oriworkService
from .utils import handleParam

def index(request):
    return render(request, 'tohocd/index.html')

def search(request):
    if 'find' in request.GET:
        word = request.GET['find']
        if 'page' in request.GET:
            num = int(request.GET['page'])
        else:
            num = 1
        form = FindForm(request.GET)
        song = songService.get_songs_byOR(word)
        params = handleParam.create_param(song, num, form, 'form')
    else:
        form = FindForm()
        params = {"form":form, "max": 0}
    return render(request, 'tohocd/search.html', params)

def detail(request):
    if len(request.GET) != 0:
        word_dict = handleParam.check_param(request.GET)
        if 'page' in request.GET:
            num = int(request.GET['page'])
        else:
            num = 1
        form = DetailForm(word_dict)
        song = songService.get_songs_byAND(word_dict)
        params = handleParam.create_param(song, num, form, 'form')
    else:
        form = DetailForm()
        params = {"form":form, "max": 0}
    return render(request, 'tohocd/detail.html', params)

def cd(request):
    if 'find' in request.GET:
        word = request.GET['find']
        form = FindForm(request.GET)
    else:
        word = ""
        form = FindForm()
    if 'page' in request.GET:
        num = int(request.GET['page'])
    else:
        num = 1
    cd = cdService.get_cds(word)
    params = handleParam.create_param(cd, num, form, 'form')
    return render(request, 'tohocd/cd.html', params)

def circle(request):
    if 'find' in request.GET:
        word = request.GET['find']
        form = FindForm(request.GET)
    else:
        word = ""
        form = FindForm()
    if 'page' in request.GET:
        num = int(request.GET['page'])
    else:
        num = 1
    circle = circleService.get_circles(word)
    params = handleParam.create_param(circle, num, form, 'form')
    return render(request, 'tohocd/circle.html', params)

def vocal(request):
    if 'find' in request.GET:
        word = request.GET['find']
        form = FindForm(request.GET)
    else:
        word = ""
        form = FindForm()
    if 'page' in request.GET:
        num = int(request.GET['page'])
    else:
        num = 1
    vocal = vocalService.get_vocals(word)
    params = handleParam.create_param(vocal, num, form, 'form')
    return render(request, 'tohocd/vocal.html', params)

def lyric(request):
    if 'find' in request.GET:
        word = request.GET['find']
        form = FindForm(request.GET)
    else:
        word = ""
        form = FindForm()
    if 'page' in request.GET:
        num = int(request.GET['page'])
    else:
        num = 1
    lyric = lyricService.get_lyrics(word)
    params = handleParam.create_param(lyric, num, form, 'form')
    return render(request, 'tohocd/lyric.html', params)

def arrange(request):
    if 'find' in request.GET:
        word = request.GET['find']
        form = FindForm(request.GET)
    else:
        word = ""
        form = FindForm()
    if 'page' in request.GET:
        num = int(request.GET['page'])
    else:
        num = 1
    arrange = arrangeService.get_arranges(word)
    params = handleParam.create_param(arrange, num, form, 'form')
    return render(request, 'tohocd/arrange.html', params)

def orisong(request):
    if 'find' in request.GET:
        word = request.GET['find']
        form = FindForm(request.GET)
    else:
        word = ""
        form = FindForm()
    if 'page' in request.GET:
        num = int(request.GET['page'])
    else:
        num = 1
    orisong = orisongService.get_orisongs(word)
    params = handleParam.create_param(orisong, num, form, 'form')
    return render(request, 'tohocd/oriSong.html', params)

def oriwork(request):
    if 'find' in request.GET:
        word = request.GET['find']
        form = FindForm(request.GET)
    else:
        word = ""
        form = FindForm()
    if 'page' in request.GET:
        num = int(request.GET['page'])
    else:
        num = 1
    oriwork = oriworkService.get_oriworks(word)
    params = handleParam.create_param(oriwork, num, form, 'form')
    return render(request, 'tohocd/oriWork.html', params)

from django.http import HttpResponse
import datetime
#from django.template.loader import get_template
#from django.template import Context'''
from django.shortcuts import render_to_response

def hello(Request):
    return HttpResponse('Hey Helen! You got me! Nice to see ya!')


def home(Request):
    return HttpResponse('This is the homepage')


def goodbye(Request):
    return HttpResponse('Goodtime here with you:)')


def current_time(Request):
    now=datetime.datetime.now()
    #t=get_template('current_datetime.html')
    #html=t.render(Context({'current_date':now}))
    #html='<html><body>It is now %s</body></html>'%now
    #return HttpResponse(html)
    return render_to_response('current_datetime.html', {'current_date': now})


def hours_ahead(Request,offset):
    try:
        offset=int(offset)
    except ValueError:
        raise Http404()
    dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
    #html="<html><body>In %s hour(s), it will be %s.</body><html>"%(offset,dt)
    return render_to_response('hours_ahead.html',{'hour_offset':offset,'next_time':dt})




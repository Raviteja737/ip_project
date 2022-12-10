from django.shortcuts import render
import requests
# Create your views here.

def ip_view(request):
    ip=request.META.get('HTTP_X_FORWARDED_FOR', "") or request.META.get ('REMOTE_ADDR')
    print(ip)
    url='http://api.ipstack.com/'+str(ip)+'?access_key=404e2d1a1361fc43bdba9d09d7009a4b'
    #url='http://api.ipstack.com/183.82.219.127?access_key=404e2d1a1361fc43bdba9d09d7009a4b'

    response=requests.get(url)
    data=response.json()
    return render(request,'testapp/test.html', data)

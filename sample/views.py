from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

import sqlite3

def shop(request):
    conn = sqlite3.connect('C:/work/sample/sqlite_shop_data.db')
    cursor = conn.cursor()
    sql = '''
        select * from shop
        order by shop_id desc
    '''
    cursor.execute(sql)
    result = cursor.fetchall()
    html = ''
    for row in result:
        html += '매장명 : %s' % row[1]
    
    cursor.close()
    conn.close()

    return JsonResponse(result, safe=False)

def data(request):
    d = { 'name': '홍', 'age': 33} 
    return JsonResponse(d)

def main(request):
    text = '''
        <ul>
            <li>1</li>
            <li>2</li>
        </ul>
    '''
    return render(request, 'main.html')
    return HttpResponse(text)

def search(request):
    #GET 방식으로 title 이라는 이름의 파라미터 전달
    title = request.GET.get('title')
    desc = request.GET.get('desc')
    print(title, desc)
    return HttpResponse('검색어 : %s, %s' % (title,desc))


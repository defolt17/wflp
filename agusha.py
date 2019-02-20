from bs4 import BeautifulSoup as bs
import numpy as np


index = 3 # Kol lig
file_name = r'Untitled.html' # Name файла в html


res = np.zeros((index, index, 3))
file = open(file_name, 'r', encoding='utf8')   
soup = bs(file.read(), 'html.parser')
score = []
rank = {
    'Вулверхэмптон':2,
    'Ньюкасл Юнайтед':3,
    'Манчестер Сити':1,
    'Челси':1,
    'Тоттенхэм':1,
    'Лестер':2,
    'Брайтон':2,
    'Бёрнли':2,
    'Кристал Пэлас':2,
    'Вест Хэм':2,
    'Ливерпуль':1,
    'Борнмут':2,
    'Саутгемптон':3,
    'Кардифф':3,
    'Уотфорд':2,
    'Хаддерсфилд':3,
    'Арсенал':1,
    'Фулхэм':3,
    'Манчестер Юнайтед':1,
    'Эвертон':2
}
#Номер группы (по нормальному) <= index


for i in soup.find_all('tr', {'class':['even stage-finished', 'odd stage-finished', 'odd no-border-bottom stage-finished', 
                                       'even no-border-bottom stage-finished']}):
    names = i.find_all('span', {'class':['padr', 'padl']})
    points = i.find_all('td', {'class':'cell_sa score bold'})
    
    if names[0].string and names[1].string and points[0].string:
        if int(points[0].string[0]) > int(points[0].string[-1]):
            score = 0
        if int(points[0].string[0]) < int(points[0].string[-1]):
            score = 1
        if int(points[0].string[0]) == int(points[0].string[-1]):
            score = 2
        
        res[int(rank[names[0].string]) - 1][int(rank[names[1].string]) - 1][score] += 1
            
        
    
print(res) 

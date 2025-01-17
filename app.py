import requests #파이썬으로 웹사이트 접속 도와주는 라이브러리
from bs4 import BeautifulSoup #파이썬으로 HTML 웹문서 분석 도와주는 라이브러리리
# 크롤러의 기본

#웹페이지 정보가 다 들어옴
데이터 = requests.get('https://finance.naver.com/item/sise.naver?code=005930') 
data = requests.get('https://www.google.com/finance/quote/019170:KRX?hl=ko')
# print(데이터.content)

#웹사이트 접속 제대로 되고 있나 확인 가능: 정상(200) 비정상(400/500)
print(데이터.status_code)


#데이터 한글 깨짐 없이 하는 방법
#1.BeautifulSoup (HTML파일(content)을 넣어야됨 , 잠깐 넣었다 빼기)
soup = BeautifulSoup(데이터.content, 'html.parser')
soup2 = BeautifulSoup(data.content, 'html.parser')
#2.HTML 속에서 필요한 정보만 싹 뽑기
print(soup.find_all('span', id="_quant")[0].text)
#_class가 YMlKec 2fh로 띄어져 있으면 하나만 입력하고 인덱싱 주의
print(soup2.find_all('div', class_="YMlKec")[1].text)


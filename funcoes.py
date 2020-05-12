from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

#url = urlopen("https://www.ifb.edu.br/brasilia/noticiasbrasilia")

def pegaPagina(url):
  try:
    resposta = url
    soup = BeautifulSoup(resposta.read(), "html.parser")
    return soup
  except:
    print("erro na função pega pagina")

'''url = open("noticias.html", "r")

soup = BeautifulSoup(url.read(), "html.parser")'''


#pega titulo
def buscarTitulo(soup):
	titulos = []
	for item in soup.select(".tileHeadline"):
		texto = item.get_text().strip()
		titulos.append(texto)
	return(titulos)
#print(titulos)

#pega link_noticia
def buscarLink(soup):
	link_noticia = []
	for item in soup.select(".tileHeadline"):
		link = (item.a.get('href'))
		link_noticia.append(link)
	return(link_noticia)

'''pegar descricao 
for item in soup.select(".description"):
  texto = item.get_text().strip()
  descricao.append(texto)
print(descricao)
#".description"''' 


#buscar horario
def buscarHorario(soup):
	horario = []
	l=[]
	for item in soup.find_all('span', class_='documentByLine'):
			l.append(item.get_text().replace('\n', '').strip())
			for x in l:
					y = ' '.join(x.split())
			horario.append(y.split())

	for i in range(0,len(horario)):
		horario[i] = "{0} {1}".format(horario[i][3], horario[i][4])
	return(horario)



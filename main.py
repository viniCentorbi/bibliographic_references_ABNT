import requests
from bs4 import BeautifulSoup
import random

def gerar_datas(intDia, intMes, intAno, qtd_datas):

	meses = ['_', 'Janeiro', 'Feveiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
	datas_finais = []

		
	for i in range(qtd_datas):

		mes = random.randint(intMes, intMes+2)

		dia = random.randint(intDia, 28)
		strMes = meses[mes]

		data = str(dia) + ' de ' + strMes + ' em ' + str(intAno)
		datas_finais.append(data)

	return datas_finais

def gerar_refencias(file, dia, mes, ano):

	input_file = open(file, 'r', encoding='utf-8')

	output_file = open('referencias_bibliograficas.txt','w',encoding='utf-8')

	datas = gerar_datas(dia, mes, ano, 30)

	i = 0

	for line in input_file:

		url = line.rstrip('\n')

		page = requests.get(url)
		soup = BeautifulSoup(page.content, 'html.parser')

		try:
			title = soup.find('title').get_text()
		except Exception as e:
			print('Erro: {e}')
			title = 'Sem título'


		print(title)

		output_file.write('"' + title + '". Disponível em: <' + url + '>. Acessado em: '+ datas[i] + '.\n')

		i+=1

	input_file.close()
	output_file.close()

#Inserir o arquivo txt com  os links e a data de início aproximada do primeiro site acessado
gerar_refencias('links.txt', 14, 9, 2021)

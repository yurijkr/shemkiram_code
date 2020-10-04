# -*- coding: UTF-8 -*-
#Tenho um problema. Não aprendi a utilizar banco de dados implemetando em código mas já estou estudando.
#Então vou criar uma lista para armazenar os dados que foram captados.
from test._test_multiprocessing import SayWhenError

''' Organizaçao do Pseudocódigo:
Pontuações Maria

Receber jogo
Receber pontos

Calcular o minimo da temporada
Calcular o maximo da temporada
Verificar quantas vezes quebrou o recorde máximo
Verificar quantas vezes quebrou o recorde mínimo
'''
#Variaveis
lista_jogo = []
lista_placar = []
recorde_min = []
recorde_max = []
recorde_min_1 = 0
recorde_max_1 = 0
#Entradas
jogo = int(input("Informe o jogo da Temporada:\n Caso queira ir para as estatísticas Digite 0.\n"))
#Processamento
while jogo != 0:
    placar = int(input("Informe o número de pontos que Maria fez nesse jogo:\n"))
    lista_jogo.append(jogo)
    lista_placar.append(placar)
    min_temp = min(lista_placar)
    max_temp = max(lista_placar)
    jogo = int(input("Informe o jogo da Temporada:\n Caso queira ir para as estatísticas Digite 0.\n"))
decisao = int(input("Informe qual relatório que deseja imprimir:\n 0- Encerrar o programa.\n 1- Placar mínimo e máximo da temporada.\n 2- Quantidade de quebra de recorde mínimo e máximo da temporada.\n\n"))
while decisao != 0:
    if decisao == 1:
        print("Placar mínimo da temporada é :{0}\n Placar máximo da temporada é: {1}\n\n".format(min_temp, max_temp))
    if decisao == 2:
        for n in lista_placar:
            if n < min_temp:
                recorde_min.append(1)
            if n > max_temp:
                recorde_max.append(1)
        recorde_min_1 = sum(recorde_min)
        recorde_max_1 = sum(recorde_max)
        print("Número de quebra de recorde mínimo foi: {0}\n Número de quebra de recorde máximo foi: {1}\n\n".format(recorde_min_1, recorde_max_1))
    decisao = int(input("Informe qual relatório que deseja imprimir:\n 0- Encerrar o programa.\n 1- Placar mínimo e máximo da temporada.\n 2- Quantidade de quebra de recorde mínimo e máximo da temporada."))          
print("Até o próximo registro de pontos. :)")

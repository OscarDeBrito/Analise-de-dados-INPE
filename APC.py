import plotly.express as px
from plotly.offline import plot
import plotly.graph_objects as go
import pandas as pd

df1 = pd.read_csv('focos2000.csv', sep=';')
df2 = pd.read_csv('focos2004.csv', sep=';')
df3 = pd.read_csv('focos2020.csv', sep=';')

df_array1 = df1.values
df_array2 = df2.values
df_array3 = df3.values

data1 = []
data2 = []
data3 = []

for l in df_array1:
    data1.append(l[0])
for l in df_array2:
    data2.append(l[0])
for l in df_array3:
    data3.append(l[0])
    
def remove_repetidos(lista): #recebe o parâmetro
    l = []
    for i in lista: #ler os elementos
        if i not in l: #se n tiver lá faz a parada
            l.append(i) # se tiver, vai pra lista 
    return l

lista1 = remove_repetidos(data1)
lista2 = remove_repetidos(data2)
lista3 = remove_repetidos(data3)

def calcula_frequencia(lista, data):
  
    frequencia1 = []
    for i in range(len(lista)):
        n = data.count(lista[i])
        frequencia1.append(n)
    return frequencia1 

#criando a variável e recebendo o resultado da função
frequencia1 = calcula_frequencia(lista1, data1)
frequencia2 = calcula_frequencia(lista2, data2)
frequencia3 = calcula_frequencia(lista3, data3)

linha1 = go.Figure([
    go.Scatter(x = lista1,y = frequencia1,name = 'Anos 2000', marker_color = '#E5FF00'),
    go.Scatter(x = lista2,y = frequencia2, name = 'Anos 2004', marker_color = '#F76FFF'),
    go.Scatter(x = lista3,y = frequencia3,name = 'Anos 2020', marker_color = '#00FA43'),
])

style = { #Estilização do Gráfico
    'font_style':'Times New Roman',
    'color_text':'#0000CD',
    'bg_color':'#D3D3D3',
    'font_size': 18
}

linha1.update_layout( #Estilização do Gráfico
    title = 'Comparação de focos de Queimadas entres os anos 2000, 2004 e 2020',
    yaxis_title = dict(text='<b>Valores em milhares<b>'),
    xaxis_title = dict(text='<b>Tempo<b>'),
    plot_bgcolor = style['bg_color'],
    paper_bgcolor = style['bg_color'],
    font_color = style['color_text'],
    font_family = style['font_style'],
    font_size = style['font_size'],
    height = 700
)
plot(linha1)











import plotly.express as px
from plotly.offline import plot
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('focos2000.csv', sep=';')

df_array = df.values

estados = []

for l in df_array:
    estados.append(l[4])

def remove_repetidos(estados):
    l = []
    for i in estados:
        if i not in l:
            l.append(i)
    return l

estados1 = remove_repetidos(estados)

def calcula_frequencia(lista, estados):
    frequencia = []
    for i in lista:
        n = estados.count(i)
        frequencia.append(n)
    return frequencia

frequencia1 = calcula_frequencia(estados1, estados)


fig = go.Figure(go.Sunburst( 
    labels = ['Estados']+estados1, #aparece o nome
    parents = ['']+['Estados']*len(estados1), #outra lista que relaciona com labels dizendo o pai de quem 
    values = [0] + frequencia1 #atribuindo os valores das listas
)) 

style = { #Estilização do Gráfico
    'font_style':'Times New Roman',
    'color_text':'#0000CD',
    'bg_color':'#D3D3D3',
    'font_size': 18
}


fig.update_layout( #Estilização do Gráfico
    title = 'Análise de Queimadas por estados em 2000',
    yaxis_title = dict(text='<b>Meses<b>'),
    xaxis_title = dict(text='<b>Focos de queimadas em centenas<b>'),
    plot_bgcolor = style['bg_color'],
    paper_bgcolor = style['bg_color'],
    font_color = style['color_text'],
    font_family = style['font_style'],
    font_size = style['font_size'],
    height = 700
)

plot(fig)













import plotly.express as px
from plotly.offline import plot
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('focos2020.csv', sep=';')

df_array = df.values

data = []

for l in df_array:
    data.append(l[0])

mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    return l

lista1 = remove_repetidos(data) #chamando a função e aplicando na lista os elementos e retornando na lista1

def calcula_frequencia(lista, data):
    frequencia = []
    for i in lista:
        n = data.count(i)
        frequencia.append(n)
    return frequencia

frequencia1 = calcula_frequencia(lista1, data)#aplicando a função os parâmetros e retornando o valor para frequancia1

fig = go.Figure(go.Bar(
            x=frequencia1,
            y=mes,
            orientation='h'),
            )

style = { #Estilização do Gráfico
    'font_style':'Times New Roman',
    'color_text':'#0000CD',
    'bg_color':'#D3D3D3',
    'font_size': 18
}

fig.update_layout( #Estilização do Gráfico
    title = 'Focos de Queimadas por mês em 2020',
    yaxis_title = dict(text='<b>Meses<b>'),
    xaxis_title = dict(text='<b>Focos de queimadas em centenas<b>'),
    plot_bgcolor = style['bg_color'],
    paper_bgcolor = style['bg_color'],
    font_color = style['color_text'],
    font_family = style['font_style'],
    font_size = style['font_size'],
    height = 700
)
plot(fig)










import plotly.graph_objects as go ##Biblioteca de Objetos Gráficos
from plotly.offline import plot ## Biblioteca Offline
import pandas as pd  ##Biblioteca do pandas
data = pd.read_csv('Queimadas.csv', sep=',') ##sep é usado como o separador que separa os objects sendo impressos pela função
data_array = data.values
biomas = []
ano = []
ano2000 = []
ano2004 = []
ano2008 = []
ano2012 = []
ano2016 = []
ano2019 = []
for linha in data_array:
    ano.append(linha[0][0:4])
    biomas.append(linha[5])
for i in range(len(ano)): #len ta contando a quantidade de elementos e o range ta fazendo uma sequencia 
    if ano[i] == '2000':
        ano2000.append(biomas[i])
    elif ano[i] == '2004':
        ano2004.append(biomas[i])
    elif ano[i] == '2008':
        ano2008.append(biomas[i])
    elif ano[i] == '2012':
        ano2012.append(biomas[i])
    elif ano[i] == '2016':
        ano2016.append(biomas[i])
    elif ano[i] == '2019':
        ano2019.append(biomas[i])
        
biomas = list(map(str, set (biomas))) #seprando os elementos repetidos, transformando em string, transforma em lista.
biomas = sorted(biomas)  #ordem alfabética
biomas.remove(biomas[-1]) #exclusão dos elementos 
biomas.remove(biomas[-1])
ano00 = []
ano04 = []
ano08 = []
ano12 = []
ano16 = []
ano19 = []
for i in range(len(biomas)):
    ano00.append(ano2000.count(biomas[i]))
    ano04.append(ano2004.count(biomas[i]))
    ano08.append(ano2008.count(biomas[i]))
    ano12.append(ano2012.count(biomas[i]))
    ano16.append(ano2016.count(biomas[i]))
    ano19.append(ano2019.count(biomas[i]))
        
fig = go.Figure()
fig.add_trace(go.Bar(
    x=biomas,
    y=ano00,
    name='2000',
    marker_color='#6A5ACD',
    marker_line_color = "#333",
))
fig.add_trace(go.Bar(
    x=biomas,
    y=ano04,
    name='2004',
    marker_color='#556B2F',
    marker_line_color = "#333",
))
fig.add_trace(go.Bar(
    x=biomas,
    y=ano08,
    name='2008',
    marker_color='#1E90FF',
    marker_line_color = "#333",
))
fig.add_trace(go.Bar(
    x=biomas,
    y=ano12,
    name='2012',
    marker_color='#00FF7F',
    marker_line_color = "#333",
))
fig.add_trace(go.Bar(
    x=biomas,
    y=ano16,
    name='2016',
    marker_color='#A9A9A9',
    marker_line_color = "#333",
))
fig.add_trace(go.Bar(
    x=biomas,
    y=ano19,
    name='2019',
    marker_color='#BA55D3',
    marker_line_color = "#333",
))
fig.update_layout(title='Queimadas nos biomas brasileiros',title_font_color='#000000',title_font_size=25,
                  paper_bgcolor='#FFFAFA', plot_bgcolor='#B0C4DE')
fig.update_yaxes(title='Número de alerta de queimadas',title_font_size=16,title_font_color='#000000')
fig.update_xaxes(title='Biomas brasileiros',title_font_size=16,title_font_color='#000000')
plot(fig)









import pandas as pd
import plotly.graph_objects as go
dados_co = pd.read_csv("historico_regiao_centro-oeste.csv")
dados_nd = pd.read_csv("historico_regiao_nordeste.csv")
dados_nt = pd.read_csv("historico_regiao_norte.csv")
dados_sd = pd.read_csv("historico_regiao_sudeste.csv")
dados_sl = pd.read_csv("historico_regiao_sul.csv")

dados_co = dados_co.values
dados_nd = dados_nd.values
dados_nt = dados_nt.values
dados_sd = dados_sd.values
dados_sl = dados_sl.values

def soma_queimadas(dados_regiao): 
  soma = 0
  for n in dados_regiao:
      soma += n[13] #somando
  return soma
soma_co = soma_queimadas(dados_co)
soma_nd = soma_queimadas(dados_nd)
soma_nt = soma_queimadas(dados_nt)
soma_sd = soma_queimadas(dados_sd)
soma_sl = soma_queimadas(dados_sl)


focos_regiao = [soma_co, soma_nd, soma_nt, soma_sd, soma_sl]
grafico = go.Figure(go.Pie(
    labels =["Centro-oeste", "Nordeste","Norte","Sudeste","Sul"],
    values = focos_regiao
))
grafico.update_layout( #Estilização do Gráfico
    title = dict(text = 'Focos Ativos Por região',
                 xanchor = 'center',
                 x = 0.5,
                 xref = 'paper'                       
    )
)
plot(grafico)
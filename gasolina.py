import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = 'gasolina.csv'
df = pd.read_csv(data)

with sns.axes_style('whitegrid'):

  grafico_gas = sns.FacetGrid(data=df, palette="pastel")
  grafico_gas.map(sns.lineplot, "dia", "venda")
  grafico_gas.set(title='Preço da gasolina na cidade de São Paulo nos 10 primeiros dias de Julho de 2021', xlabel='Dia', ylabel='Preço');
  grafico_gas.fig.set_size_inches(w=15/2.54, h=7.5/2.54)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# lendo o arquivo .csv e criando dataframe
gasolina_df = pd.DataFrame(pd.read_csv("gasolina.csv"))
gasolina_df

# Criando o gráfico de linha para a variação do preço da gasolina
sns.set(style="whitegrid")     #Definindo o grid branco
plt.figure(figsize=(8, 6))     # Determinando o tamanho da figura
sns.lineplot(data=gasolina_df, x='dia', y='venda', marker='o', markersize=8, color='b', label='Preço da Gasolina') # Gerando o gráfico
plt.xlabel('Dia')     # Definindo os nomes do eixo x
plt.ylabel('Preço')   # Definindo o nome do eixo y


plt.savefig("gasolina.png")   #Salvando em png

plt.show()            # Mostrando o gráfico
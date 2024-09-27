import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('C:/Users/Ikky/Documents/Ebac_10/ecommerce_preparados.csv')
df.head()
df.tail()

# >>Grafico de Barras
plt.figure(figsize=(10, 10))
df['Nota'].value_counts().plot(kind='bar' , color= '#90ee70' )
plt.title('Barras - Nota')
plt.xlabel('Nota')
plt.ylabel('Quatidade')
plt.show()

# >> Mapa de Calor
heat = df[['Qtd_Vendidos_Cod','N_Avaliações_MinMax']].corr()
sns.heatmap(heat, annot=True, cmap='coolwarm')
plt.title('heatmap')
plt.show()

# >>Grafico de pizza
x= df['Gênero'].value_counts().index
y= df['Gênero'].value_counts().values

plt.pie(y,labels=x, autopct='%.1f%%', startangle=0)
plt.title('Gênero')
plt.show()

# >>Grafico de densidade
sns.kdeplot(df['N_Avaliações_MinMax'], fill=True, color='#00FF00')
plt.title('Densidade Avaliações')
plt.xlabel('Avaliaçãoes')
plt.show()

# >>Grafico de Dispersão
sns.jointplot(x='N_Avaliações', y='Gênero', data=df, kind='scatter')
plt.show()
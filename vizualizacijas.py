import pandas as pd # datu apstrāde
from termcolor import colored as cl # teksta izvade
import matplotlib.pyplot as plt # vizualizācija
import seaborn as sb # vizualizācija

# vizualizaciju pamata konfigurācija
sb.set_style('whitegrid') # plot style
plt.rcParams['figure.figsize'] = (15, 10) # plot size


# Karstuma karte (korelācija)
def karstuma_karte(datne, saglabat=False):
    df = pd.read_csv(datne)
    sb.heatmap(df.corr(method = 'spearman'), annot = True, cmap = 'coolwarm')
    if saglabat:
        # izveidojam datnes nosaukumu bez mapes un faila tipe
        datnes_vards = datne[datne.find("/"):datne.find(".")]
        plt.savefig('atteli/{}-heatmap.png'.format(datnes_vards))
    plt.show()


# Lieluma sastopamības biežums
def sadalijuma_grafiks(datne, kolonna, saglabat=False):
    df = pd.read_csv(datne)
    sb.distplot(df[kolonna], color = 'r')
    plt.title(kolonna.capitalize() + ' biežums', fontsize = 16)
    plt.xlabel(kolonna.capitalize(), fontsize = 14)
    plt.ylabel('Biežums', fontsize = 14)
    plt.xticks(fontsize = 12)
    plt.yticks(fontsize = 12)
    if saglabat:
        plt.savefig('atteli/{}.png'.format(kolonna))
    plt.show()


# Izkliedes grafiks (scatter plot)
def izkliedes_grafiks(datne, x, y, saglabat=False):
    df = pd.read_csv(datne)
    i = df.columns
    
    plot1 = sb.scatterplot(x, y, data = df, color = 'orange', edgecolor = 'b', s = 15)
    plt.title('{} / {}'.format(x, y), fontsize = 16)
    plt.xlabel('{}'.format(x), fontsize = 14)
    plt.ylabel('{}'.format(y), fontsize = 14)
    plt.xticks(fontsize = 12)
    plt.yticks(fontsize = 12)
    if saglabat:
        plt.savefig('atteli/{}-{}.png'.format(x, y))
    plt.show()


datne1 = 'dati/auto_simple.csv'
datne2 = 'dati/auto_imports.csv'
datne3 = 'dati/auto_imports_degviela.csv'
datne4 = 'dati/auto_imports_tips.csv'
datne6 = 'dati/ss_lv_auto.csv'
datne7 = 'dati/atbildes.csv'

karstuma_karte(datne6, True)
sadalijuma_grafiks(datne6, "nobraukums")
# sadalijuma_grafiks(datne2, "price")
# izkliedes_grafiks(datne1, 'Volume', 'CO2')
# izkliedes_grafiks(datne1, 'Weight', 'CO2')
# izkliedes_grafiks(datne2, 'price', 'horsepower')
izkliedes_grafiks(datne6, 'cena', 'gads')
izkliedes_grafiks(datne6, 'cena', 'nobraukums')
izkliedes_grafiks(datne6, 'gads', 'cena')
# izkliedes_grafiks(datne3, 'price', 'fuel-type')
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 13:46:42 2023

@author: tomde
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot

fullFilenamePath = './B52_DDN6_TP.ohm'  # Chemin depuis ce code vers le fichier des données
labelERT = 'R (Ohm)'
labelIP = 'IP (mV/V)'

# Importer le jeu de données via pandas:
#
#   - Si le jeux de données contient ERT et IP et que le jeu contient des estimations d'erreur,
#   les paramètres a entrer sont ceux utilisés ci-dessous.
#
#   - Si le jeux de données contient moins de données,
#   il faut ajuster les paramètres skiprows et names en fonction.
#
data = pd.read_csv(
    fullFilenamePath,
    delimiter='\t',
    header=None,
    skiprows=36, 
    names= [
        'a', 'b', 'm', 'n',
        labelERT, 'Res. Error (Ohm)',
        labelIP, 'IP Error (mV/V)'],
    index_col=False,
    skipfooter=0,
    engine='python')
nbInit = len(data.index)
print(f'Initial number of values: {nbInit}')
print(data.describe())

# Montrer les histogrammes:

# 1) Résistance: 
binsR = np.logspace(
    start=np.log(min(data[labelERT])),
    stop=np.log(np.quantile(data[labelERT], 0.9)),
    num=20)
hist1 = data.hist(
    column=[labelERT],
    bins=binsR,
    density=False)

# 2) IP:
hist2 = data.hist(
    column=[labelIP],
    density=False)

pyplot.show()

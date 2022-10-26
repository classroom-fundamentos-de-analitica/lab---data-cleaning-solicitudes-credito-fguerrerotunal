"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
from datetime import datetime


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col = 0)
    
    df.dropna(axis = 0, inplace = True)
    
    for columna in ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'barrio', 'línea_credito']:
            df[columna] = df[columna].str.lower()
            df[columna] = df[columna].apply(lambda x: x.replace('_', ' '))
            df[columna] = df[columna].apply(lambda x: x.replace('-', ' '))
    
    remplace = ['$',',','\.00',' ']
    for i in remplace:
        df["monto_del_credito"] = df.monto_del_credito.str.replace(i, '')
    
    df.estrato = df.estrato.astype(int)
    df.comuna_ciudadano = df.comuna_ciudadano.astype(int)
    df.monto_del_credito = df.monto_del_credito.astype(int)
    
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(lambda x: datetime.strptime(x, "%Y/%m/%d") if len(x.split("/")[0]) == 4 else datetime.strptime(x, "%d/%m/%Y"))
    
    df.drop_duplicates(inplace=True)

    return df

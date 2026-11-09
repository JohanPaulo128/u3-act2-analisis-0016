#import librerias
import pandas as pd
import numpy as np
print("Analisis de diagnostico de salud Johan Paulo NC 0016")

pacientes = {
    "Nombre": ["Ana", "Luis", "Marta", "Roberto", "Carla", "Javier"],
    "Presion_Arterial": [120, 140, 135, 110, 150, 155],
    "Fumador": [False, True, False, False, True, True],
    "Nivel_Riesgo": ["Bajo", "Alto", "Medio", "Bajo", "Alto", "Alto"]
}
df = pd.DataFrame(pacientes)
print(df)
print("+-+-+-+Agrupar por una sola columna+-+-+-+-+")
agrupado = df.groupby('Nivel_Riesgo')
print(agrupado)
print("+-+-+-+por agregacion+-+-+-+")
# Average salary by department
print(agrupado['Presion_Arterial'].mean())
# Maximum age in each department
print(agrupado['Presion_Arterial'].max())

print("+-+-Segunda parte+-+-+Johan Paulo Aros Reveles NC 0016+-+-+-+")
print("Agregacion multiples")
print("mean-->promedio, sum -->")
resultado_agrgado = agrupado['Fumador'].agg(['mean','sum','max','min'])
print(resultado_agrgado)
print("Agrupacion por varias columnas")
print("Agrega columna al DataFrame")
# Create another column
df['Equipo'] = ['A','B','A','B','A','B']

agrupado_multiple = df.groupby(['Fumador', 'Equipo'])['Fumador'].mean()
print(agrupado_multiple)
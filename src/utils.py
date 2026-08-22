notas = [
    {"alumno": "Ana",  "asignatura": "mates", "nota": 7},
    {"alumno": "Luis", "asignatura": "mates", "nota": 5},
    {"alumno": "Ana",  "asignatura": "lengua", "nota": 9},
    {"alumno": "Luis", "asignatura": "lengua", "nota": 6},
    {"alumno": "Eva",  "asignatura": "mates", "nota": 8},
]

def media_por(datos, columna_grupo, columna_valor):

    sumas = {}
    conteos = {}

    for fila in datos:
        clave = fila[columna_grupo]
        sumas[clave] = sumas.get(clave, 0) + fila[columna_valor]
        conteos[clave] = conteos.get(clave,0) +1

    media = { grupo: round(sumas[grupo]/ conteos[grupo],2) for grupo in sumas}

    return media

    



print(media_por(notas, "asignatura", "nota"))  # {'mates': 6.67, 'lengua': 7.5}
print(media_por(notas, "alumno", "nota"))      # {'Ana': 8.0, 'Luis': 5.5, 'Eva': 8.0}
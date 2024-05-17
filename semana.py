
# Defineno los nombres de los días de la semana
dias_semana = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]

#  eventos de mis  día de la semana
eventos_semana = [
    [ "descanso ", ],  # Domingo
    [  "clases con ingles",  ],  # Lunes
    [ "Clases con Baces de Datos", ],  #martez
    [ "Algebra lineal ", ],#miercoles
    [ "Estrutura de Datos", ],  # jueves
    [ "Semillero ", ],  # viernes
    [ "Hacer Tareas", ],  # viernes
       
]

for dia, eventos in zip(dias_semana, eventos_semana):
    print(f"{dia}: {', '.join(eventos)}")

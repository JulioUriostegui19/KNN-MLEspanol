"""
Aqui encontraras algunas funciones que facilitarán la implementacion
del algoritmo. 

De: MLEspanol
07.02.2024
"""

import numpy as np
import matplotlib.pyplot as plt

# dictionary para el texto del plot
def dim2Name(argument):
    switcher = {
        1: "Peso del vehiculo" , 
        2: "Peso de carga maximo",
        3: "Tiempo de vuelo maxima",
        4: "Rango maximo",
        5: "Velocidad"
    }
    return switcher.get(argument, "NULL")
    
# funcion para graficar los datos
def plot(hybrid,fix,multy, dim1, dim2):

	# graficar
	plt.scatter(hybrid[:,dim1], hybrid[:,dim2], marker="o", c="#00B050")
	plt.scatter(fix[:,dim1],fix[:,dim2], marker="s",c="#6B004D")
	plt.scatter(multy[:,dim1],multy[:,dim2], marker="^", c="#D7B722")

	plt.xlabel(dim2Name(dim1))
	plt.ylabel(dim2Name(dim2))
	leg=plt.legend(["Hybrid", "Fixed-Wing","Multirotor"], frameon= False, loc="lower right")

# funcion para evaluar el modelo
def test_modelo(prediccion, etiquetas_test):
    s = 0
    for i in range(len(prediccion)):
    
        # comparar resultados con clase real
        print(prediccion[i] == etiquetas_test[i])
        s+=1.
       
        # mensaje de error 
        if (prediccion[i] != etiquetas_test[i]): 
            print("Prediccion: "+ str(prediccion[i]) +"; Etiqueta real: " + str(etiquetas_test[i]))
            s-=1.
    print("Puntuacion: ", s/len(prediccion))

# funcion para crear un UAV
def UAV(peso, carga, resistencia, rango, velocidad,min, max):
    atributos=np.array([peso, carga, resistencia, rango, velocidad])
    for i in range(len(atributos)):
        # normalizacion de los resultados
        atributos[i]=(atributos[i]- min[i])/(max[i]-min[i])
      
    return np.reshape(atributos,[-1,1]).T

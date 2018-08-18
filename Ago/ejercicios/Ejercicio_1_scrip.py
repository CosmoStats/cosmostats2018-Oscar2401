#Oscar De la Cruz Echeveste Viernes 17 de agsto 2018

import matplotlib. pyplot as plt
import numpy as np
import random


#MATRICES:
#__________________________________________________________________________
#Funciones utiles:

#Creando función para llenado de matrices.
def fillmx(n,m,A):
    for i in range(n):
        a=[] #se creea una lista que corresponde a cada fila de la matriz.
        for j in range(m):
            print(i+1,j+1, end=' = ')
            a.append(float(input())) #El usuario insertará los datos.
        A.append(a) 

#Creando función para imprimir matriz.
def prmx(A):
    for i in range(len(A)):
        print(A[i])

###### Multiplicación de matrices ######

#Creando función que multiplica matices.
def mxm(n,m,v,A,B):
    C=[]
    for i in range(n):
        a=[]   #Crea una lista que corresponde a cada fila de la matriz.
        for j in range(v):
            sum=float(0)   #Acomulador de las sumas de multiplicación de elementos de matriz. 
            for k in range(m):
                sum=(A[i][k]*B[k][j])+sum
            a.append(sum)
        C.append(a)
    return C

#Cuerpo del programa Multiplicación de matrices.
M1=[]
M2=[]
M3=[] 

print('###### Este programa multiplica matrices ######\n\n')
n=int(input('Matriz 1 de nxm: \nNum. de filas n: '))   #El usuario ingresa el tamaño de la matriz.
m=int(input('Numero de columnas m: '))  
fillmx(n,m,M1)   #El usuario llena la matriz. 
u=int(input('Matriz 2 mxp: \nNum. de filas m: '))
v=int(input('Num. de Columnas p: '))
if m!=u:
        print('La multiplicación no se puede realizar.\n')
        print('El número de columnas de la matriz 1 debe ser igual al número de filas de la Matriz 2.\n')
else:
        fillmx(u,v,M2)   #El usuario llena la matriz.
        M3=mxm(n,m,v,M1,M2)   #Se hace la multiplicación
        print('\nMatriz Resultante=\n')
        prmx(M3)   #Se imprime la matriz resultante.

###### Determinante de una matriz ######

#Creando función determinante:
def det(A):
    i=0
    j=0
    k=0
    sum=0   #acomulador de suma.
    if len(A[0]) == 2:   #Determinante de una matriz 2x2.
        sum=((A[0][0]*A[1][1])-(A[0][1]*A[1][0]))  
        
    if len(A[0])>2:   #Si la matriz A es nxn con n>2 el determinante es más complejo.
        for k in range(len(A[0])):   #La cantidad de números (multiplicando el subdeterminate) que se suman es el número de columnas de la matriz.
            B=[]   #Se crea una matriz de cofactores B de (n-1)x(n-1) para tambien obtener su deteminante.
            for i in range(len(A[0])-1):   
                a=[]
                for j in range(len(A[0])-1):
                    if k<=j:
                        a.append(A[i+1][j+1])   
                    if k>j:
                        a.append(A[i+1][j])
                B.append(a)
            if k%2==0:   #Si k (el número de columna de A) es par incluyendo el cero entonces el signo es positivo
                sum=sum+((A[0][k])*det(B))
            if k%2!=0:   #Si k (el número de columna de A) es par incluyendo el cero entonces el signo es negativo
                sum=sum-((A[0][k])*det(B))
    return sum


#Cuerpo del programa Determinante
print('###### Este programa calcula el determinante de matrices ######')
M=[]
n=int(input('Matriz cuadrada de nxn:\nn:  '))
fillmx(n,n,M)
prmx(M)
print('\nEl determinante de la matriz es: ',det(M))

#Gráficas:
#__________________________________________________________________________

#Graficar un círculo.
t=np.arange(0,1.01,0.01) #arreglo de 0 a 1 incrementando 0.01 
x=np.cos(2*np.pi*t) #parametrización del círculo
y=np.sin(2*np.pi*t)
plt.plot(x,y,'r')
plt.fill_between(x,y,color='g') #Rellena el círculo de color g=green
plt.show()

#Puntos Aleatorios.
u=np.arange(0,1.01,0.01)   #llena un arreglo de 0 a 1.01 incrementando en 0.01
v=np.arange(0,1.01,0.01)
random.shuffle(u)  #Mueve aleatoriamente los datos en el arreglo u
random.shuffle(v)
plt.text(0.03,0.8,'Puntos al aleatorios')
plt.plot(u,v,'g*')
plt.show()



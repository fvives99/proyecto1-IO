
import numpy as np
import sys


def open_file(file_name):
    file1 = open(file_name, 'r')
    Lines = file1.readlines()
    i = 0
    while(i<len(Lines)):
        Lines[i] = [int(e) if e.isdigit() else e for e in Lines[i].split(',')]
        i+=1
    return Lines


if sys.argv[1] == "-h":
    print(" El archivo de código fuente a ejecutarse debe llamarse simplex.py, ejecutando de la forma:\n"+"python simplex.py [-h] archivo.txt")
    Lines = open_file(sys.argv[2])
    out = open("out_"+sys.argv[2], 'w')
else:
    Lines = open_file(sys.argv[1])
    out = open("out_"+sys.argv[1], 'w')

#matriz = [[1, 2, -43,78],
 #[4, 5, -56, 5],
 #[7, 8, 10, 200],
 #[99, 10, 9, 8]]


#filaPivote = [3, 2, 0, 0, 1, 18]
matriz = [[-3, -5, 0, 0, 0, 0],
 [1, 0, 1 , 0, 0 , 4],
 [0, 2, 0, 1,0,12],
 [3, 2, 0, 0, 1, 18]]
matriz_np = np.array(matriz)
matriz_np=np.float64(matriz_np)
filaPivote = []
#pivote = 0
#def imprimir_matriz(matriz):
   #  for columna in range(len(matriz[0])):
   #     for fila in range(len(matriz)):
    #        print(matriz[columna][fila], end=" ")
    #    print()
#imprimir_matriz(matriz)


#Necesito enviar la fila en la que está el pivote
def cambiar_fila(matriz,fila, numeroFilaPivote):
    

    #print("\n\n",fila)

    #print("\n\n", numeroFilaPivote)
    
    #print(matriz)
    #nueva_matriz = []
    for i in range(len(matriz)):
        if(i == numeroFilaPivote):
            #arreglo = np.array(matriz[i])
            #nueva_matriz.append(arreglo.tolist())
            j = 0
            while j < len(fila):
                #print(fila[j])
                matriz[i][j]= fila[j]
                j += 1
    #print("\n\nNUEVA\n",matriz)
    


        #else: 
             #nueva_matriz.append(fila)
             
    #matriz = nueva_matriz
    #print("\n\n",matriz)
    #print("Finalizado")
    #print(matriz[2][0])
    #print(fila)

    #NO BORRAR
    #for i in range(len(fila)):
       # print(fila[i])

    #i= numeroFilaPivote
   # for i in range(len(fila)):
    #    for j in range(len(matriz[0])):
    #        matriz[i][j] = fila[i]
   # print("\n\n",matriz)
            

    

#cambiar_fila(matriz_np)

#largo = [1, 45, 7]
def determinar_solucion(matriz):
    #print("\n\nOriginal\n",matriz)
    menorActual = 0
    posicionMenorEnColumna = 0
    #Sacamos al menor de U
    for x in range(len(matriz[0])):
        if matriz[0][x] <= 0 and matriz[0][x] < menorActual:
            menorActual = matriz[0][x]
            posicionMenorEnColumna = x
    #print(menorActual)
    #print(posicionMenorEnColumna)
    if(menorActual >= 0):
        
        print("Decimos que ya termino, pero falta implementar")
        return 1
    else:
        #print("ESTAMOS DESARROLLANDO")
        
        
        #columnaMenor es columnaPivote y columnaResultado es el LD
        columnaMenor = matriz[:,posicionMenorEnColumna]
        columnaResultado = matriz[:,(len(matriz[0]))-1]
        
        #print("ESTAMOS REVISANDO",columnaMenor)
        #print(columnaResultado)
        pivote = 100000
        numeroFila = 0
        #Acá sacamos al pivote y los respectivos valores de la división de LD / columna pivote
        for i in range(len(matriz)):
           # print("\nElemento de la Columna Pivote en la iteración: ",columnaMenor[i])
           #print("Elemento de columna resultado: ",columnaResultado[i])
           # print("Columna Resultado: ", (columnaResultado[i] / columnaMenor[i]))
           if columnaMenor[i] > 0 and (pivote > (columnaResultado[i] / columnaMenor[i])) and ((columnaResultado[i] / columnaMenor[i]) > 0): 
                    pivote = columnaMenor[i]
                    filaPivote = matriz[i]
                    numeroFila= i
                   # print("Fila pivote:",filaPivote)
                    #print("Pivote: ", pivote)
                   # print("Resultado de LD/elementos de la columna pivote: ",columnaResultado[i] / columnaMenor[i])
                   # print("Número de fila del pivote: ", i)
                    
        
        #ARREGLAR PORQUE SOLO ES PARA MxM
        #print("\n",filaPivote)
        
        #NO BORRAR
        # nuevaFila = []    
        #i =0
        #while i < len(filaPivote):
            #nuevaFila.append(filaPivote[i] / pivote)
            
            #i+=1
        
        #print(nuevaFila)

        y = 0
        z = 0
        m = 0
        nuevaFila = [] 
        filaPivoteNueva= []
        print(numeroFila)

        while y < len(matriz):
            if y == numeroFila:
                while z < len(filaPivote):
                    #print("\n\n",filaPivote[z] / pivote,"\n\n", "FIla\n\n",filaPivote[z], "\n\nPivote\n\n",pivote)
                    nuevaFila.append(filaPivote[z] / pivote)
                    filaPivoteNueva.append(filaPivote[z] / pivote)
                    z +=1
                    #print("Llegó")
                cambiar_fila(matriz, nuevaFila, numeroFila)
                nuevaFila = [] 
                #print("ES NUEVA FILA", nuevaFila, "XD")
                   
            y+=1
      
        while m < len(matriz):
            if m != numeroFila:
                n =0
                
                while n < len(filaPivote):
                    #print(columnaMenor[m])
                    #print("+[0m Columna REsultado ", columnaResultado[m])
                    nuevaFila.append(matriz[m][n]+(-columnaMenor[m]*filaPivoteNueva[n]))
                    n += 1
                    #print("LlegóXDDDDDDDDDDDDD")
            cambiar_fila(matriz, nuevaFila, m)
            #print("ES NUEVA FILA", nuevaFila, "XDDDDDDDD")
            nuevaFila = [] 
            
            m += 1
    print(matriz)
    determinar_solucion(matriz)
    
###############
 #       i =0
   #     while i < len(filaPivote):
  #          nuevaFila.append(filaPivote[i] / pivote)
   #         
    #        i+=1
        
    #    print(nuevaFila)

    #return cambiar_fila(matriz,nuevaFila,numeroFila)

##########
#def cambiarFilas(matriz,filaPivote,numeroFilaPivote,pivote):
  #  i = 0
   # nuevaFila = [] 
   # print("PAsó")
   # while i < 1:
      #  print("Llegó")
      #  if i != 4:
      #      print("IF")
       #     nuevaFila.append(filaPivote[i] / pivote)
       #     cambiar_fila(matriz, nuevaFila, numeroFilaPivote)
       #     nuevaFila = []
        #    x = 0
       #     while x < len(filaPivote):
         #       if(i != numeroFilaPivote):
           #         print("ENTRANDO")
          #      x += 1
        #else:
           # i+=1
#
            
determinar_solucion(matriz_np)
#cambiarFilas(matriz_np, filaPivote,4,2)



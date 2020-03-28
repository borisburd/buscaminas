# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 14:46:28 2020

@author: Boris Lmao
"""

import random
import numpy as np

def pos_random(filas , columnas):
    x_random = random.randint (0 , filas-1)
    y_random = random.randint (0 , columnas-1)
    return (x_random , y_random)

def crear_tablero_minado(filas , columnas , bombas):
    t = np.repeat(0 , filas * columnas)
    t = t.reshape(filas , columnas)
    for i in range (bombas):
        pos = pos_random(filas , columnas)
        t[pos] = -1
    return t

def en_rango (tablero , coord):
    n_filas = tablero.shape[0]
    n_columnas = tablero.shape[1]
    check = False
    if coord[0] < n_filas and coord[0] >= 0:
        if coord[1] < n_columnas and coord[1] >= 0:
            check = True
    return check

def vecinos_de ( tablero , coord ):
    lista_vecinos = []
    lista_pos_columnas = [-1 , 0 , 1 , 1 , 1 , 0 , -1 , -1]
    lista_pos_filas = [-1 , -1 , -1 , 0 , 1 , 1  , 1 , 0]
    for i in range(8):
        coord_vecino = (coord[0] + lista_pos_filas[i] , coord[1] + lista_pos_columnas[i])
        check = en_rango (tablero , coord_vecino)
        if check:
            lista_vecinos.append(coord_vecino)
    return lista_vecinos

def cant_minas_vecinas (tablero , coord):
    lista_vecinos = vecinos_de (tablero , coord)
    cant_minas = 0
    for i in range(len(lista_vecinos)):
        if tablero[lista_vecinos[i]] == -1:
            cant_minas += 1
    return cant_minas

def poner_numeros(tablero):
    for i in range(tablero.shape[0]):
        for j in range(tablero.shape[1]):
            if not tablero[(i,j)] == -1:
                n_minas = cant_minas_vecinas (tablero , (i , j))
                tablero[(i,j)] = n_minas
                
def crear_tablero_oculto(filas , columnas, bombas):
    tablero = crear_tablero_minado(filas , columnas , bombas)
    poner_numeros(tablero)
    return tablero

def crear_mapa(tablero):
    filas = tablero.shape[0]
    columnas = tablero.shape[1]
    mapa = np.repeat("." , filas * columnas)
    mapa = mapa.reshape (filas , columnas)
    return mapa

def seguir_jugando (mapa , tablero_oculto):
    check = False
    while check == False:
        for i in range (mapa.shape[0]):
            for j in range (mapa.shape[1]):
                if mapa[(i , j)] == ".":
                    if tablero_oculto[(i,j)] != -1:
                        check = True
    print(check)
    return check

def tocar (mapa , tablero_oculto , coord):
    if tablero_oculto[coord] == -1:
        mapa[coord] = "X"
        check = False
    elif tablero_oculto[coord] == 0:
        mapa[coord] = tablero_oculto[coord]
        tocar_vecinos(mapa , tablero_oculto , coord)
    
        
        
        check = True
    else:
        mapa[coord] = tablero_oculto[coord]
        check = True
    return check

def tocar_vecinos(mapa , tablero , coord):
    vecinos = vecinos_de(tablero , coord)
    for i in range(len(vecinos)):
        if mapa[vecinos[i]] == ".":
            tocar(mapa , tablero , vecinos[i])
                
    
    

    
    
def pedir_coordenada():
    f = int(input("Ingrese el numero de fila: "))
    c = int(input("Ingrese el numero de columna: "))
    return (f,c)

def jugar(filas, columnas, bombas):
    oculto = crear_tablero_oculto(filas , columnas , bombas)
    mapa = crear_mapa(oculto)

    exploto = False
    while not exploto and seguir_jugando(mapa , oculto):
        print(mapa)
        coord = pedir_coordenada()
        if en_rango(oculto , coord):
            seguimos = tocar(mapa , oculto , coord)
            if not seguimos:
                print("buuuuuum!")
                exploto = True
        else:
            print("Coordenadas fuera de rango.")
    print(mapa)
    if exploto:
        print(" Veras los malbones crecer desde abajo")
    else:
        print(" Lo lograste campeon ")
    return exploto

    
    
    
    


    
            
    
            

filas = 10
columnas = 10
bombas = 2           
   
jugar(filas, columnas , bombas)                                  
















    
    
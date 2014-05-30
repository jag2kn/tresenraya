#! /usr/bin/env python
# -*- coding: utf-8 -*

import random

'''
Codigo basado en:
https://raw.githubusercontent.com/aitiba/tresenraya/master/index.py
'''

def main(matrix):
		
	
	matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
	
		
	salir = False

	print "=== Tres en linea. ==="

	turno = bool(random.getrandbits(1))

	while not salir:
	
		if turno:
			print "\n== Turno para usuario =="
			imprimirMatriz(matrix)
			x = int(raw_input('Escriba coordenada en x [0,1,2] '))
			y = int(raw_input('Escriba coordenada en y [0,1,2] '))
			
			if matrix[y][x]==0:
				matrix[y][x]=1
				turno = not turno;
				print "\n== Turno para el computador =="
			else:
				print "\nPosición ya ocupada\n"
		else:
			x = int(random.random()*3)
			y = int(random.random()*3)
			
			
			if matrix[y][x]==0:
				matrix[y][x]=-1
				turno = not turno;
			else:
				print ".",
				
		res = winner(matrix)
	
		if res != 0:
		
			print "\n"
		
			imprimirMatriz(matrix)
			
			print "\n"
	
			if res [1][0] == 1:
				print 'HAS GANADO! :-)'
			else:
				print 'HAS PERDIDO! :-('
			print res[0]
			print ' == GANADOR ' + str(res[1][0]) + ' =='
			salir = True

	print "Fin del programa"


'''
	Funciones de test
'''
def win(which):
	if which == 'LINEA':
		matrix = [[0, 0, -1], [1, 1, 1], [-1, -1, 0]]
	elif which == 'CRUZADA':
		matrix = [[0, -1, 1], [-1, 1, 0], [1, 0, -1]]
	elif which == 'ARRIBABAJO':
		matrix = [[0, 1, -1],[-1, 1, 0],[0, 1, -1]]
			
	print '\n'.join([repr(e) for e in matrix])
	return matrix

def lose(which):
	if which == 'LINEA':
		matrix = [[0, 0, 1], [-1, -1, -1], [0, 1, 1]]
	elif which == 'CRUZADA':
		matrix = [[0, 1, -1], [1, -1, 0], [-1, 0, 1]]
	elif which == 'ARRIBABAJO':
		matrix = [[0, -1, 1],[1, -1, 0],[0, -1, 1]]
			
	print '\n'.join([repr(e) for e in matrix])
	return matrix


def imprimirMatriz(matrix):
	print "Matriz actual: \n"
	for x in matrix:
		for y in x:
			if y==1:
				t = "X"
			elif y==-1:
				t = "O"
			else:
				t = "-"
			
			print "\t"+t,
		print "\n"
	print "\n"

def winner(matrix):
	matrix_cruzado = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
	matrix_arribaAbajo = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
	a = 0
	for x in matrix:
		#Guarda la arriba de arriba abajo
		#y cruzandamente de un lado al otro

		matrix_arribaAbajo[0][a] = x[0]
		matrix_arribaAbajo[1][a] = x[1]
		matrix_arribaAbajo[2][a] = x[2]
		
		if a == 0: 	
			matrix_cruzado[0][0] = x[0]
			matrix_cruzado[1][0] = x[2]
		if a == 1:
			matrix_cruzado[0][1] = x[1]
			matrix_cruzado[1][1] = x[1]
		if a == 2:
			matrix_cruzado[0][2] = x[2]
			matrix_cruzado[1][2] = x[0]
		a = a + 1;
		
		#LINEA RECTA
		#balioa = [0, 1, 2]
		#print all([ balioa == 0 for a in x ])
		if x[0] == x[1] == x[2] and x[0] == x[1] == x[2] != 0:
			return ["LINEA RECTA", x]

	#LINEA DE ARRIBA ABAJO
	for x in matrix_arribaAbajo:
		if x[0] == x[1] == x[2] and x[0] == x[1] == x[2] != 0:
			return ["LINEA DE ARRIBA ABAJO", x]

	#LINEA CRUZADA
	for x in matrix_cruzado:
		if x[0] == x[1] == x[2] and x[0] == x[1] == x[2] != 0:
			return ["LINEA CRUZADA", x]

	return 0

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
main(matrix)




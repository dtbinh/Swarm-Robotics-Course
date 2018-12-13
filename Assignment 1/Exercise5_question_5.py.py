# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 19:55:04 2018

@author: kamal
"""

import numpy as np 
import matplotlib.pyplot as plt

E_53 = [[0, 2], [1, 2], [2, 3], [2, 4], [6, 7],[6, 8], [4, 5]]

x_0 = [20, 10, 15, 12, 30, 12, 15, 16, 25]
dt = 0.001
n_vertices = 12

#eigen_value function
def eigen_values(L):
    
    l, w= np.linalg.eig(L)
    l.sort()
    y  = list(enumerate(l))
    for i in y:
        print('{}) eigen values is: {}'.format(i[0], i[1]))

# question 4 subquestion 4
def cycle_graph(n):
    E = []

    for i in range(n):
        if i != n-1:
            E.append([i,i+1])
        else:
            E.append([i,0])
    return E

#Question 4
def get_laplacian(E, n_vertices, flag):
    
    A = np.zeros((n_vertices, n_vertices)) # adjancency matrix
    D = np.zeros((n_vertices, n_vertices)) # degree matrix
    laplacian = np.zeros((n_vertices, n_vertices))

    
    if flag == False:
        # calculate the degree matrix for undirected graph
        for each_vertex in range(n_vertices): # For each_vertex we calculate the degree of that vertex
            degree = 0 

            for i in list(range(0, len(E))):
                for j in list(range(0, 2)):
                    if(E[i][j] == each_vertex):
                        degree += 1
            D[each_vertex][each_vertex] = degree
        
        # Calculate the adjancency matrix
        for each_vertex in range(len(E)):
            x, y= E[each_vertex][0], E[each_vertex][1]

            A[x][y] = 1 
            A[y][x] = 1 

        laplacian = np.subtract(D, A)
        return laplacian
        #print("The laplacian for undrirected graph is\n", laplacian)

    if flag == True:
        #Calculate the degree matrix for directed graph
        for each_vertex in range(n_vertices):
            degree_head = 0

            for i in list(range(len(E))):
                if(E[i][1] == each_vertex):
                    degree_head += 1
            D[each_vertex][each_vertex] = degree_head

        #Calculate the Adjancency matrix
        for each_vertex in range(len(E)):
            x = E[each_vertex][0]
            y = E[each_vertex][1]

            A[y][x] = 1
        
        laplacian = np.subtract(D, A)
        return laplacian
        

def simulate_consensus(x_0, T, L, dt=0.001):

    n_step = int(T/dt)
    x = [n_step*[0] for i in range(9)]

    #x_0 = [20,10,15,12,30,12,15,16,25] #state of robot at initial stage
    
    for i in range(len(x_0)):
        x[i][0] = x_0[i]
    
    for step in range(1,int(T/dt)):
        for r in range(9):
            if(r == 0):
                x[0][step] = x[0][step-1] + dt*(x[2][step-1] - x[0][step-1])
            elif(r == 1):
                x[1][step] = x[1][step-1] + dt*(x[2][step-1] + x[3][step-1] - 2*x[1][step-1])
            elif (r == 2):
                x[2][step] = x[2][step-1] + dt*(x[0][step-1] + x[1][step-1] + x[3][step-1] + x[4][step-1] - 4*x[2][step-1])
            elif(r == 3):
                x[3][step] = x[3][step-1] + dt*(x[2][step-1] + x[1][step-1] - 2*x[3][step-1])
            elif(r == 4):
                x[4][step] = x[4][step-1] + dt*(x[2][step-1] + x[5][step-1] - 2*x[4][step-1])
            elif(r == 5):
                x[5][step] = x[5][step-1] + dt*(x[4][step-1] - x[5][step-1])
            elif(r == 6):
               x[6][step] = x[6][step-1] + dt*(x[7][step-1] + x[8][step-1] - 2*x[6][step-1])
            elif(r == 7):
                x[7][step] = x[7][step-1] + dt*(x[6][step-1] - x[7][step-1])    
            elif(r == 8):
                x[8][step] = x[8][step-1] + dt*(x[6][step-1] - x[8][step-1])
    t = [i*0.001 for i in range(int(T/dt))]
    
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.plot(t, x[0], label="robot 1")
    plt.plot(t, x[1], label="robot 2")
    plt.plot(t, x[2], label="robot 3")
    plt.plot(t, x[3], label="robot 4")
    plt.plot(t, x[4], label="robot 5")
    plt.plot(t, x[5], label="robot 6")
    plt.plot(t, x[6], label="robot 7")
    plt.plot(t, x[7], label="robot 8")
    plt.plot(t, x[8], label="robot 9")
    
    legend = plt.legend(loc='upper right', shadow=True)
    legend.get_frame().set_facecolor('#ffffff')
	
    plt.show()
    #print("The convergence for 1st subgraph is",x[0][-1])
    #print("The convergence for 2st subgraph is",x[8][-1])
    print(eigen_values(get_laplacian(E_53, 9, False)))

L = get_laplacian(E_53, 9, False)
simulate_consensus(x_0, 50, L, dt)

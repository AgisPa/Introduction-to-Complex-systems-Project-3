#Subroutine that calculates time-dependent order parameter values

import numpy as np
import dist
import random

#Initialization in order to keep track of the realizations of the 4th and 5th subquestion
randint=[0,1,2,3,4,5,6,7,8,9,10]

def euler(N,kappa,g,T,dt,input,seed):

    #Initialization
    random.seed(seed)
    Nt=int(T/dt)
    kappa = kappa
    th = np.zeros([N,Nt])
    rt=[0 for j in range(Nt)]

    #Defines the initial phases
    for i in range(0,N):
        th[i][0]=(i)/N*2*np.pi
    if input=="d":
        rand = np.random.choice(randint)
        randint.remove(rand)
        for i in range(0, N):
            th[i][0] = (i) / N * 2 * np.pi* rand/10

    #Defines the natural frequency distribution for each case
    if input=="a" or input=="b":
        w = dist.natural(N)
    if input=="c" or input=="d":
        w=dist.uniform(N,g)
    if input=="e":
        rand = np.random.choice(randint)
        randint.remove(rand)
        w=dist.uniform(N,g)

    #Time iterative process using the Euler method
    for j in range(1,Nt):
        for i in range(0,N):
            cor=0
            for k in range(0,N):
                cor=cor+np.sin((th[k][j-1]-th[i][j-1]))
            th[i][j]=th[i][j-1]+ dt* (w[i] + kappa * cor/N)
        rt[j]=sum(np.e** (th[n][j]*1j) for n in range(N))/N
        rt[j]=abs(rt[j])
    if input=="a" or input=="c":
        return rt[Nt-1]
    if input=="b" or input=="d" or input=="e":
        return rt


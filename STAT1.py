import numpy as np
from scipy.stats import gamma
import matplotlib.pyplot as plt


def gamma(a:int,b,n):
    M=np.random.exponential(1/b,[n,a]) #n lignes a colonnes
    L = []
    for i in range(n):
        Y=np.sum(M[i])
        L.append(Y)
    return L
     

def estimateurs(L):
    
    n = len(L)
    u = sum(L) / n
    o = sum(x**2 for x in L ) / n
    
    a_chap= (u**2) / (o - u **2)
    b_chap = u / (o - u**2)

    return a_chap, b_chap

# Exemple d'utilisation
donnees = [1.5, 2.3, 3.1, 4.2, 5.0]
a, b = estimateurs(donnees)

print("Estimation du paramètre a :", a)
print("Estimation du paramètre b :", b)


def risque(a , b , n , m):
    liste_a_chap = []
    liste_b_chap = []
    for i in range(m):
        L = gamma(a, b ,n)
        a_chap = estimateurs(L)[0]
        liste_a_chap.append(a_chap)
        b_chap = estimateurs(L)[1]
        liste_b_chap.append(b_chap)
        
        l_a = [(a_chap - a)**2 for a_chap in liste_a_chap]
        l_b = [(b_chap - b)**2 for b_chap in liste_b_chap]
        
        r_a = np.sqrt(np.mean(l_a))
        r_b = np.sqrt(np.mean(l_b))
        
        return [r_a , r_b]
    
R = risque(10 , 5, 10, 100)
print(R)
print("\n preciision de a =" , R[0] , "\n")
print("\n preciision de b =" , R[1] , "\n")
           

#Application
#on doit mettre le fichier txt dans le meme dossier que le TP

file = open('redundantsystem.txt')
L= file.readlines()
K=[float(x) for x in L]

#file.close()
#l’estimation du modèle sous-jacent à leur fonctionnement
k = estimateurs(K)
print(k)

# la moyenne des durées de fonctionnement est relativement petite par rapport 
#à la moyenne des carrés des durées de fonctionnement,cequi entraîne une valeur
#relativement élevée pour b_chap

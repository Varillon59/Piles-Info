def pilevide():
    return []

def estvide(P):
    return P==pilevide()

def empiler(P,e):
    return P.append(e)

def depiler(P):
    return(P.pop())


def lire_sommet_pile(P):
    if estvide(P):
        return estvide(P)
    else:
        A=depiler(P)
        empiler(P,A)
        return A

def dupliquer_pile(P):
    A=pilevide()
    L1=pilevide()
    Pdup=pilevide()
    while estvide(L) == False:
        main=depiler(P)
        empiler(A,main)
        empiler(L1,main)
    while estvide(L1) == False:
        empiler(P,depiler(L1))
    while estvide(A) == False:
        empiler(Pdup,depiler(A))
    return Pdup

def taille_pile(P):
    n=0
    A=pilevide()
    while estvide(P) == False:
        empiler(A,depiler(P))
        n+=1
    while estvide(A) == False:
        empiler(P,depiler(A))
    return n

def inverse_pile(P):
    A=pilevide()
    Pnorm=pilevide()
    while estvide(P) == False:
        empiler(A,depiler(P))
    while estvide(A) == False:
        empiler(Pnorm,depiler(A))
    while estvide(Pnorm) == False:
        empiler(P,depiler(Pnorm))
    return P

def element_in_stack(P,e):
    rep=0
    A=pilevide()
    while estvide(P) == False:
        main=depiler(P)
        if main != e:
            empiler(A,main)
        else:
            rep+=1
            empiler(A,main)
    while estvide(A) == False:
        empiler(P,depiler(A))
    if rep != 0:
        return True
    else:
        return False

def k_element_in_stack(P,e):
    A=pilevide()
    element=0
    if estvide(P):
        return "Vide"
    else:
        for i in range(e):
            empiler(A,depiler(P))
        element=lire_sommet_pile(A)
        while estvide(A) == False:
            empiler(P,depiler(A))
    return element

def parenthesage(chaine):
    A=pilevide()
    for i in chaine:
        if i == "(":
            empiler(A,i)
        elif i == ")":
            if A != pilevide():
                depiler(A)
    if A == pilevide():
        result="Oui"
    else:
        result="Non"
    return result

def evaluation(RPN):
    A=pilevide()
    for i in RPN:

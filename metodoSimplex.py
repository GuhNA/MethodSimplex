#Gustavo Henrique Nascimento de Almeida RA:106296

import math
exp = int(int(input("Digite a quantia de restrições: ")))
var = int(input("Digite a quantia de variáveis: "))
#quantia de colunas = quantia de variáveis + quantia de expressões(var aux) + z e b;
c = var + exp + 2
#linhas = funcão Z + restrições
l = exp + 1


def printM(matrix, x):
    print(x)
    for i in matrix:
        for j in i:
            print(f"{j:.2f}", end = " ")
        print()
    print()

def menorCol(matrix):
    valor = math.inf 
    for i in range(l):
        for j in range(c):
            if(j != c-1):
                if(matrix[i][j] < valor):
                    valor = matrix[i][j]
                    pos = j
    return pos

def divB(matrix):
    j = menorCol(matrix)
    if(matrix [1][c-1] / matrix[1][j] < matrix [2][c-1] / matrix[2][j]):
        pos = [1,j]
    else:
        pos = [2,j]
    return pos

def divAll(matrix):
    pos = divB(matrix)
    a = pos[0]
    b = pos[1]
    div = matrix[a][b]
    for i in range(c):
        matrix[a][i] = matrix[a][i] / div
    
    return a

def divOthers(matrix):
    j = menorCol(matrix)
    m = divAll(matrix)
    for i in range(l):
        if(m != i):
            inverso = matrix[i][j]
            #formula  NLx = (Lx* -1 *matrix[i][j] + matrix[i][j])
            for k in range(c):
                matrix[i][k] += matrix[m][k] * -1 * inverso

def verificaN(matrix):
    for i in matrix[0]:
        if(i < 0):
            return True
    return False

def methodSimplex(matrix):
    while(verificaN(matrix)):
        divOthers(matrix)

    printM(matrix, "Solução final:")
    for i in range(c):
        cont = 0
        for j in range(l):
            cont += matrix[j][i]
        if(cont == 1):
            match(i):
                case 0: print(f"Zmax = {matrix[i][c-1]:.2f}")
                case _: print(f"x{i} = {matrix[i][c-1]:.2f} ")
        if(cont > 1 or cont < 1):
            if(i < var+1):
                match(i):
                    case _: print(f"x{i} = 0")



matrix = []
msg = ""
let = ""
print("Caso não possua a variavel colocar 0!")
for i in range(l):
    linha = []
    for j in range(c):
        match(i):
            case 0: msg = "expressão Z"
            case _: msg = f"expressão {i}"

        if(i == 0):
            if(j == 0):
                 linha.append(1.)
                 continue
        
        #os 1 dos auxiliares, z + var + i -1(-1 pq começa na segunda linha)
        if(j == 1+var+i-1 and i != 0):
            linha.append(1.)
            continue

        if(j == (c-1) and i != 0):
            let = "b"
        elif(j < var+1 and j!= 0): let = "x" + str(j)
        else: 
            linha.append(0.)
            continue

        if(i == 0 and j != c-1): #realmente neceesario esse j != ?
            linha.append(-1* float(input(f"Para {msg} digite o valor de {let}: ")))
        else:
            linha.append(float(input(f"Para {msg} digite o valor de {let}: ")))

        #repassar todos os valores da lista, se for none, inserir 0;

    matrix.append(linha)




printM(matrix, "Problema inicial:")
methodSimplex(matrix)
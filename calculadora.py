#importações
from math import sqrt, log
import time

#titulo
print('-=-' * 7)
print('Priemira Calculadora!')
print('-=-' * 7)

time.sleep(1)

while True:

    #possiveis açoes
    print("""Operações possíveis!
#Soma [+]
#Subtração[-]
#Multiplicação [*]
#Divisão [/]
#Porcentagem [%]
#Potenciação [**]
#Radiciação [!]
#Log [Log]""")

    #petição de numero e função
    time.sleep(1)
    a = float(input('Primeiro número: '))
    op = str(input('Digite a operação: ')).strip().title()

    if op in '+ Soma Mais Somar':
        b = float(input('Segundo número: ')) #caso +, -, *, /, etc. ele pergunta o segundo numero
        resultado = a + b

    elif op in '- Menos Subtracao Subtração Subtrair':
        b = float(input('Segundo número: '))
        resultado = a - b

    elif op in '* × . X Vezes Multiplicacao Multiplicação Multiplicar':
        b = float(input('Segundo número: '))
        resultado = a * b

    elif op in '% Porcentagem Porcento':
        b = float(input('Segundo número: '))
        resultado = (a / 100) * b

    elif op in '^ ** Potencia Potência Potenciacao Potenciação':
        b = float(input('Segundo número: '))
        resultado = a ** b  

    elif op in '/ ÷ : Divisao Divisão Dividir Dividido':
        b = float(input('Segundo número: '))

        if b != 0: 
            resultado = a / b

        else:  #numeros divisiveis por 0 dão erro
            print('Erro, tente novamente!')

    elif op in 'Log Logarítmica Logritma Logaritmo Logaritmica Logarítimica Logritima Logaritimo Logaritimica':
        b = float(input('Segundo número: '))
        resultado = log(a, b)  

    elif op in '! Raiz Radiciação Radiciacao': #função radiciação sem o b
        resultado = sqrt(a)      

    else: #qual quer coisa q fuja de numeros nas funçoes a e b dão erro
        print('Erro, tente novamente!')
        continue
    
    #print processando com um time de 2segundos
    print('PROCESSANDO...')
    time.sleep(2)          
    print('O resultado foi {:.2f}'.format(resultado))
    
    #pergunta se quer continuar
    continuar = str(input('Deseja continuar (S/N)? ')).strip().lower()
    if continuar != 's':
        print('Programa encerrado.')
        break

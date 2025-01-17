# #controle de fluxo: usando IF
x = -3

# verificando condições 
if x <= 0:
    print("é menor que zero")
elif x <= 2:
    print("é menor que dois")
else:
    print("maior")


# Usando FOR

for i in range(1,5): #range não deixa chegar até o último elmento
    print(i)

lista_de_alunos = ["Roger", "Romana", "Guilherme"] 
for aluno in lista_de_alunos: # no caso em questão, aluno é uma variável que só exsitirá dentro do for, no momento de iteração.
    print(aluno)


# Usando WHILE
import time

condicao = True
while condicao:
    print("Execute minha ETL")
    time.sleep(5)

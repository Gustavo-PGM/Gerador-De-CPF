import random
numeros = ''

#Fazer vários cpf's, ex: for _ in range(100):
for i in range(9):
    numeros += str(random.randint(0, 9))

multi_1 = 10
resul_1 = 0
for digitos_1 in numeros:
    resul_1 += int(digitos_1) * multi_1
    multi_1 -= 1
    resto_1 = resul_1 * 10 % 11 if multi_1 <= 1 else 0


multi_2 = 11
resul_2 = 0
for digitos_2 in numeros + str(resto_1):
    resul_2 += int(digitos_2) * multi_2
    multi_2 -= 1
    resto_2 = resul_2 * 10 % 11 if multi_2 <= 1 else 0

print(f'O seu CPF gerado é: {numeros[:3]}.{numeros[3:6]}.{numeros[6:9]}-{resto_1}{resto_2}')

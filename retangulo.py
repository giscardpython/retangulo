def calcular_retangulo(base, altura):
    area = base * altura
    return area

calcular_retangulo2 = lambda base, altura: base * altura

# programa principal
base = int(input('Informe a base do retângulo: '))
altura = int(input('Informe a altura do retângulo: '))

print(f'Área do retângulo:  {calcular_retangulo2(base, altura)}')
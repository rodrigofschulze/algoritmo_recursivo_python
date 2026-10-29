def troco(moedas, x):
    if x == 0:
        return 0

    if x < 0:
        return float('inf')

    minimo = float('inf')

    for moeda in moedas:
        resultado = troco(moedas, x - moeda)
        minimo = min(minimo, resultado + 1)

    return minimo


moedas = {1, 3, 4}
x = 10

print(troco(moedas, x))
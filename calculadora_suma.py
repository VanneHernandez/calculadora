def suma_acumulada(n):
    if n == 1:
        return 1
    else:
        return n + suma_acumulada(n - 1)

numero = 5
resultado = suma_acumulada(numero)
print(resultado)
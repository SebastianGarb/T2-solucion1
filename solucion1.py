import random

def min_max_m3(lst, x=0):
    if x == len(lst):
        return float('inf'), float('-inf') 
    else:
        min_r, max_r = min_max_m3(lst, x+1)
        val = lst[x]
        
        if val % 3 == 0:
            return min(val, min_r), max(val, max_r)
        else:
            return min_r, max_r

n = int(input("Ingrese el tamaño del arreglo: "))
arreglo = [random.randint(10, 9999) for _ in range(n)]
print(f"Arreglo: {arreglo}")

minimo, maximo = min_max_m3(arreglo)

if minimo == float('inf'):
    print("No hay múltiplos de 3 en el arreglo.")
else:
    promedio = (minimo + maximo) / 2
    print(f"Resultado = ({maximo}+{minimo})/2 = {promedio}")
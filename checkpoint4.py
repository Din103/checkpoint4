# Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.
mi_lista = ['azucar', 'harina', 'levadura']
mi_tuple = ('azucar', 'harina', 'levadura')
float = 110.3
entero = 2
decimal = 0.5
mi_diccionario = {
  "Jugador1": "Pedro",
  "Jugador2": "Juan",
  "Jugador3": "Lucas",
  "Jugador4": "Mario",
  }
# Exercise 2: Round your float up.
import math
print(math.ceil(float))
# Exercise 3: Get the square root of your float.
print(math.sqrt(float))
# Exercise 4: Select the first element from your dictionary.
jugador= mi_diccionario['Jugador1']
print(jugador)
# Exercise 5: Select the second element from your tuple.
print(mi_tuple[1])
# Exercise 6: Add an element to the end of your list.
mi_lista.append("nueces")
print(mi_lista)
# Exercise 7: Replace the first element in your list.
mi_lista[0] = "sacarina"
print(mi_lista)
# Exercise 8: Sort your list alphabetically.
mi_lista.sort()
print(mi_lista)
# Exercise 9: Use reassignment to add an element to your tuple.
mi_tuple = mi_tuple + ("nueces",)
print(mi_tuple)

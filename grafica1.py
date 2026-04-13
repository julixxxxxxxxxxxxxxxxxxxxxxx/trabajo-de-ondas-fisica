import matplotlib.pyplot as plt
import numpy as np

#definimos las variables que vamos a usar, en este caso ponemos el nombre claro para que se entienda de cara a la entrega
tiempo = np.linspace(0, 10, 100)
Amplitud = 2
w = 2 * np.pi / 5
x = Amplitud * np.sin(w * tiempo)

#con las funciones estudiadas anteriormente vamos a crear el grafico de la función seno con los parámetros definidos
plt.plot(tiempo, x, label='Senoidal', color='purple', linewidth=3)
plt.title('Movimiento Armónico Simple')
plt.xlabel('Tiempo (s)')
plt.ylabel('desplazamiento (m)')
plt.legend()
plt.show()
import sys
import os
from PIL import Image
#1 Definir lo que vamos a introducir, variable 1 será la carpeta desde donde coger las imágenes y la variable 2 será la carpeta donde meter las
folder_from = sys.argv[1]
folder_to = sys.argv[2]
# print(folder_from)
# print(folder_to)

#2 Tenemos que ver si la carpeta donde introducir las nuevas imágenes existe (la primera vez no) y si eso crearla y sino no.
if not os.path.isdir(folder_to):
#aquí también podríamos haber usado os.path.exists()
    os.mkdir(f'{folder_to}')
#también podríamos haber usado os.makedirs()

#3 Loop dentro de la carpeta con las imágenes y convirtiendo
current = os.getcwd()
#print(current)
entries = os.listdir(folder_from)
for i in entries:
    all_name = os.path.basename(i)
    name = os.path.splitext(i)[0]
    img = Image.open(f'./{folder_from}/{all_name}')
    img.save(f'./{folder_to}/{name}.png','png')


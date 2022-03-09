palabras=["perro", "gato", "ornitorrinco", "eucalipto", "murcielago", "ciclopentanoperhidrofenantreno", "cerebro","computacion","padel"]
vidas=6
import random
palabra_elegida=random.choice(palabras)
cantidad_letras=len(palabra_elegida)
lista_de_letras = []
print("Imagino que ya conoceras las reglas pero debes probar letras hasta que aciertes la palabra, cada error resta una vida.")
print("Si te quedas sin vidas, pierdes, ¡SUERTE!")
empezar=input("Para comenzar escribe EMPEZAR ")

if __name__ == '__main__':
    if empezar == "EMPEZAR":
        print("La palabra es " + '_ ' * cantidad_letras)
        while True:
            letra = input("Escribe la letra que quieras probar")
            lst = []
            for pos, char in enumerate(palabra_elegida):
                if char == letra:
                    lst.append(pos)
            if lst:
                lista_de_letras.append(letra)
                palabra = ""
                for letra in palabra_elegida:
                    if letra in lista_de_letras:
                        palabra = palabra + letra
                    else:
                        palabra = palabra + "_ "
                print(palabra)
                if palabra == palabra_elegida:
                    print("¡Felicidades has ganado!")
                    break
            if not lst:
                if not letra == "Ñ":
                    vidas = vidas - 1
                    print("Te quedan " + str(vidas) + " vidas restantes")
                    if vidas == 0:
                        print("Has perdido la palabra era "+ palabra_elegida)
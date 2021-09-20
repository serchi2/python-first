#Comentario, empezamos el picoteo en python
# el hola mundo mitiquisiimo
def funcionPrueba(name):
    return ("funcionPrueba "+ name)

def tutorial():
    print("hola mundo");
    #Variables, en java seria int i = 1 aqui es:
    variable1 = int(2)
    print(variable1)
    v2 = float(2.5)
    texto ="hola esto es una prueba"
    print(texto)
    texto2 = str(127)
    print(texto+texto2+" yeeeeeeepale")
    #si concatenamos un numero al imprimir va a dar error siempre, para eso se usa str(num)
    #listas en python
    ferrary=["hola1", "hola2"]
    v3=ferrary[0]
    print(v3)
    ferrary.append("yeeeeeee")
    '''lista[i]: Devuelve el elemento que está en la posición i de la lista.
    lista.pop(i): Devuelve el elemento en la posición i de una lista y luego lo borra.
    lista.append(elemento): Añade elemento al final de la lista.
    lista.insert(i, elemento): Inserta elemento en la posición i.
    lista.extend(lista2): Fusiona lista con lista2.
    lista.remove(elemento): Elimina la primera vez que aparece elemento.'''
    #Diccionarios
    diccionario = {'prueba 1':'key1', 'prueba2': 'key2'}
    var4 = diccionario.get('prueba2')
    print(var4)
    '''diccionario.get(‘key’): Devuelve el valor que corresponde con la key introducida.
    diccionario.pop(‘key’): Devuelve el valor que corresponde con la key introducida, y luego borra la key y el valor.
    diccionario.update({‘key’:’valor’}): Inserta una determinada key o actualiza su valor si ya existiera.
    «key» in diccionario: Devuelve verdadero (True) o falso (False) si la key (no los valores) existe en el diccionario.
    «definicion» in diccionario.values(): Devuelve verdadero (True) o falso (False) si definición existe en el diccionario (no como key).'''
    #identacion
    pruebaIf=1
    if(pruebaIf==1):
        print("obvio que iba a salir esto")
    else:
        print("eto que eeeeeeeeee")

    #Bucle while en python
    vuelta =1
    while vuelta <4:
        print("vuelta"+str(vuelta))
        vuelta+=1
    #en los bucles for no es posible hacer bucle infinito porque automaticamente te suma 1
    forelta=1
    for forelta in range(1,6):
        print ("forelta "+str(forelta))

    import os
    import calculadora
    print(os.getuid())
    resulModu=calculadora.calcu2(vuelta,forelta)
    print (vuelta)
    print (forelta)
    print(resulModu)

    print(funcionPrueba("hola"))

    pruebaInput = input("Prueba input: ")
    print("imprimo lo que me das por input: "+ pruebaInput)
print("solo se imprime lo que esta fuera de un def")
tutorial()
print("solo quiero ver si al hacer un commit sobre esta rama pasa algo")


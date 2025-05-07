#Función 1
def ocultarMensaje(Mensaje, Oculto):
    Mensaje = (input("Por favor ponga un mensaje:"))
    Oculto = (input("Por favor ponga el mensaje que desea ocultar"))
    if(Mensaje == "" or Oculto == ""):
        return "Le falto algún dato de poner"
    mensajeOculto = ""
    mensajeBinario = ""
    for letra in Oculto:
        binario = format(ord(letra), '08b')#El resultado que me va a dar viene en paréntesis así que no es un int
        mensajeBinario = mensajeBinario + binario
    indiceParaElMensaje = 0
    for letra in Mensaje:
        if(indiceParaElMensaje < len(mensajeBinario)):#Lo uso como condición como si fuera un while
            bit = mensajeBinario[indiceParaElMensaje]
            if(bit == '0'):
                mensajeOculto = mensajeOculto + letra + '\u0020'#No se pone el +
            else:
                mensajeOculto = mensajeOculto + letra + '\u200B'#Si pongo la u en mayúscula no hago la misma función
            indiceParaElMensaje = indiceParaElMensaje + 1
        else:
            mensajeOculto = mensajeOculto + letra
    return mensajeOculto
#print(ocultarMensaje('Este es un texto de prueba', 'OK'))

"""Le pregunté a ChatGPT que me explicara como podría pasar de binarios de nuevo numeros
   y me dijo que podía usar int y poner el binario en base 2 debido a que en el sistema
   binario el valor de cada posicion de un binario corresponde a una potencia de dos y
   que aumenta su valor de derecha a izquierda
   """

def extraerMensaje(mensajeOculto):
    if(mensajeOculto == ""):
        return ""
    mensajeExtraido = ""
    mensajeBinario = ""
    for numerodelMensaje in range(1, len(mensajeOculto), 2):#Este rango me ayuda a recorrer solo los espacios donde estan los binarios
        letra = mensajeOculto[numerodelMensaje]       
        if(letra == '\u0020'):
            mensajeBinario = mensajeBinario + '0'
        elif(letra == '\u200B'):
            mensajeBinario = mensajeBinario + '1'
        if(len(mensajeBinario) == 8):
            numeroNormal = int(mensajeBinario, 2)
            caracter = chr(numeroNormal)
            mensajeExtraido = mensajeExtraido + caracter
            mensajeBinario = "" #Vacio mensajeBinario porque si no se acumulan los bits de ciclos anteriores
    return mensajeExtraido

            
        
#print(extraerMensaje('E s​t e  ​e​s​ ​u n​  t e​x t​o​ de prueba'))




#Función 3
def ocultarInformacion(Lista,Mensaje):
    if(Lista == [] or Mensaje == ""):
        return "Le faltan datos de indicar" 
    if not (isinstance(Lista, list)):#Uso el isinstance para que el valor de la lista solo sea númerico
        return "Debe de poner una lista"
    for elemento in Lista:
        if not(isinstance(elemento,int)):
            return "Ponga un valor númerico"
    if not (isinstance(Mensaje, str)):
        return "Debe poner caracteres"
    mensajeOculto = []
    mensajeBinario = []
    for letra in Mensaje:
         binario = format(ord(letra), '08b')
         for bit in binario:  #Para recorrer el binario y pasar cada bit a un int
             mensajeBinario.append(int(bit))  
    indiceParaLista = 0
    for numeroDeLaLista in Lista:#Acodarme que esto agarra el cada seccion de los numeros de la lista uno por uno
        if indiceParaLista >= len(mensajeBinario):#Esto lo puse porque me di cuenta que si no había una condicion asi podian haber problemas si los bits se acababan
            break
        ultimoDigito = numeroDeLaLista % 10 
        if(ultimoDigito != mensajeBinario[indiceParaLista]):
            numeroDeLaLista = numeroDeLaLista - ultimoDigito + mensajeBinario[indiceParaLista]
        mensajeOculto.append(numeroDeLaLista)
        indiceParaLista = indiceParaLista + 1#Moví la indentación de este indice porque me daba errores
    return mensajeOculto

#print(ocultarInformacion([123, 456, 789, 101, 112, 131, 415, 999],'A'))


def extraerInformacion(listaConMensajeOculto):
    if(listaConMensajeOculto == []):
        return ""
    if not (isinstance(listaConMensajeOculto, list)):
        return "Por favor poner un dato que si sea una lista"
    for elemento in listaConMensajeOculto:
        if not(isinstance(elemento, int)):
            return "Por favor poner solo números en la lista"
    mensajeExtraido = ""
    mensajeBinario = []
    bitComoString = ""
    for numeroDeLaLista in listaConMensajeOculto:
        ultimoDigito = numeroDeLaLista % 10
        mensajeBinario.append(ultimoDigito)
        if(len(mensajeBinario) == 8):
            for bit in mensajeBinario:
                bitComoString = bitComoString + str(bit)#Paso el mensaje binario a string porque entonces no puedo pasarlo a binario
            numeroNormal = int(bitComoString, 2)
            caracter = chr(numeroNormal)
            mensajeExtraido = mensajeExtraido + caracter
            mensajeBinario = []
    return mensajeExtraido

#print(extraerInformacion([120, 451, 780, 100, 110, 130, 410, 991]))
            
#Función 5


    


    



             

    









    







     

   







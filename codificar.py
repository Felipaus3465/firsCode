#Creado por Luis Felipe Calderon Perez
#Fecha de creación 12-4-21 10:20
#Última fecha de modificación 18-4-21 3:20
#Importacion de librerias
import pickle 
import time
#Apertura del archivo.dat
f=open('Bitacora.dat','wb')
#Definicion de funciones
def opcionCodificarCodigoMurcielago():
    """
    Funcionamiento: Recibe el código escrito por el usuario
    Entrada: Código escrito por el usuario
    Salida: Imprime la variable AuxCodMur y al finalizar llama al menu
    Restricción: Si la variable AuxCodMur retorna vacío, llama a opcionCodificarCodigoMurcielago
    """
    palabra=input('Escriba el texto a codificar: ')
    AuxCodMur=opcionCodificarCodigoMurcielagoAux(palabra)
    print(AuxCodMur)
    if AuxCodMur=='':
        return opcionCodificarCodigoMurcielago()
    pickle.dump(time.strftime("%H:%M:%S")+' '+'Murcielago-Cod : entra('+palabra+')'+',sale('+AuxCodMur+')',f)
    return menu()
def opcionCodificarCodigoMurcielagoAux(palabra):
    """
    Funcionamiento: Válida el código escrito por el usuario
    Entrada: palabra
    Salida: Llama a la función codificarCodigoMurcielago
    """
    palabra=palabra.upper()
    if len(palabra)==0:
        print('El texto debe contener información')
        return ''
    for i in palabra:
        if i.isdigit():
            print('El texto no puede contener números')
            return ''
    return codificarCodigoMurcielago(palabra)
def codificarCodigoMurcielago(palabra):
    """
    Funcionamiento: Codifica el código escrito por el usuario
    Entrada: palabra
    Salida: acumulador
    """
    codigo=['M','U','R','C','I','E','L','A','G','O']
    valor=['0','1','2','3','4','5','6','7','8','9']
    acumulador=''
    for i in range(len(palabra)):
        if palabra[i] in codigo[0]:
            acumulador+=palabra[i].replace(palabra[i],valor[0])
        elif palabra[i] in codigo[1]:
            acumulador+=palabra[i].replace(palabra[i],valor[1])
        elif palabra[i] in codigo[2]:
            acumulador+=palabra[i].replace(palabra[i],valor[2])
        elif palabra[i] in codigo[3]:
            acumulador+=palabra[i].replace(palabra[i],valor[3])
        elif palabra[i] in codigo[4]:
            acumulador+=palabra[i].replace(palabra[i],valor[4])
        elif palabra[i] in codigo[5]:
            acumulador+=palabra[i].replace(palabra[i],valor[5])
        elif palabra[i] in codigo[6]:
            acumulador+=palabra[i].replace(palabra[i],valor[6])
        elif palabra[i] in codigo[7]:
            acumulador+=palabra[i].replace(palabra[i],valor[7])
        elif palabra[i] in codigo[8]:
            acumulador+=palabra[i].replace(palabra[i],valor[8])
        elif palabra[i] in codigo[9]:
            acumulador+=palabra[i].replace(palabra[i],valor[9])
        elif palabra[i].isspace():
            acumulador+='*'
        else:
           acumulador+=palabra[i] 
    return (acumulador)
def opcionDecodificarCodigoMurcielago():
    """
    Funcionamiento: Recibe el código escrito por el usuario
    Entrada: Código escrito por el usuario
    Salida: Imprime la variable AuxDecodMur y al finalizar llama al menu
    Restricción: Si la variable AuxDecodMur retorna vacío, llama a opcionDecodificarCodigoMurcielago
    """
    codigoMur=input('Ingrese el codigo a decodificar: ')
    AuxDecodMur=opcionDecodificarCodigoMurcielagoAux(codigoMur.upper())
    print(AuxDecodMur)
    if AuxDecodMur=='':
        return opcionDecodificarCodigoMurcielago()
    pickle.dump(time.strftime("%H:%M:%S")+' '+'Murcielago-Dec : entra('+codigoMur+')'+',sale('+AuxDecodMur+')',f)
    return menu()
def opcionDecodificarCodigoMurcielagoAux(codigoMur):
    """
    Funcionamiento: Válida el código escrito por el usuario
    Entrada: codigoMur
    Salida: Llama a la función decodificarCodigoMurcielago
    """
    if len(codigoMur)==0:
        print('El texto debe contener informacion')
        return ''
    return decodificarCodigoMurcielago(codigoMur)
def decodificarCodigoMurcielago(codigoMur):
    """
    Funcionamiento: Codifica el código escrito por el usuario
    Entrada: codigoMur
    Salida: acumulador
    """
    valor=['M','U','R','C','I','E','L','A','G','O']
    codigo=['0','1','2','3','4','5','6','7','8','9']
    acumulador=''
    for i in range(len(codigoMur)):
        if codigoMur[i] in codigo[0]:
            acumulador+=codigoMur[i].replace(codigoMur[i],valor[0])
        elif codigoMur[i] in codigo[1]:
            acumulador+=codigoMur[i].replace(codigoMur[i],valor[1])
        elif codigoMur[i] in codigo[2]:
            acumulador+=codigoMur[i].replace(codigoMur[i],valor[2])
        elif codigoMur[i] in codigo[3]:
            acumulador+=codigoMur[i].replace(codigoMur[i],valor[3])
        elif codigoMur[i] in codigo[4]:
            acumulador+=codigoMur[i].replace(codigoMur[i],valor[4])
        elif codigoMur[i] in codigo[5]:
            acumulador+=codigoMur[i].replace(codigoMur[i],valor[5])
        elif codigoMur[i] in codigo[6]:
            acumulador+=codigoMur[i].replace(codigoMur[i],valor[6])
        elif codigoMur[i] in codigo[7]:
            acumulador+=codigoMur[i].replace(codigoMur[i],valor[7])
        elif codigoMur[i] in codigo[8]:
            acumulador+=codigoMur[i].replace(codigoMur[i],valor[8])
        elif codigoMur[i] in codigo[9]:
            acumulador+=codigoMur[i].replace(codigoMur[i],valor[9])
        else:
           acumulador+=codigoMur[i] 
    acumulador=acumulador.replace('*',' ')
    return (acumulador.lower())
def opcionCodificarCodigoEucalipto():
    """
    Funcionamiento: Recibe el código escrito por el usuario
    Entrada: Código escrito por el usuario
    Salida: Imprime la variable AuxCodEuc y al finalizar llama al menu
    Restricción: Si la variable AuxCodEuc retorna vacío, llama a opcionCodificarCodigoEucalipto
    """
    codigoEucalipto=input('Escriba el texto a codificar: ')
    AuxCodEuc=opcionCodificarCodigoEucaliptoAux(codigoEucalipto)
    print(AuxCodEuc)
    if AuxCodEuc=='':
        return opcionCodificarCodigoEucalipto()
    pickle.dump(time.strftime("%H:%M:%S")+' '+'Eucalipto-Cod : entra('+codigoEucalipto+')'+',sale('+AuxCodEuc+')',f)
    return menu()
def opcionCodificarCodigoEucaliptoAux(codigoEucalipto):
    """
    Funcionamiento: Válida el código escrito por el usuario
    Entrada: codigoEucalipto
    Salida: Llama a la función codificarCodigoEucalipto
    """
    if len(codigoEucalipto)==0:
        print('El código  eucalipto debe conter información')
        return ''
    for i in codigoEucalipto:
        if i.isdigit():
            print('En el código  eucalipto no se admite texto alfanumérico')
            return ''
    return codificarCodigoEucalipto(codigoEucalipto.upper())
def codificarCodigoEucalipto(codigoEucalipto):
    """
    Funcionamiento: Codifica el código escrito por el usuario
    Entrada: codigoEucalipto
    Salida: acumulador
    """
    codigo=['E','U','C','A','L','I','P','T','O','Á','É','Í','Ó','Ú']
    valor=['1','2','3','4','5','6','7','8','9']
    acumulador=''
    for i in range(len(codigoEucalipto)):
        if codigoEucalipto[i] in codigo[0]:
            acumulador+=codigoEucalipto[i].replace(codigoEucalipto[i],valor[0])
        elif codigoEucalipto[i] in codigo[1]:
            acumulador+=codigoEucalipto[i].replace(codigoEucalipto[i],valor[1])
        elif codigoEucalipto[i] in codigo[2]:
            acumulador+=codigoEucalipto[i].replace(codigoEucalipto[i],valor[2])
        elif codigoEucalipto[i] in codigo[3]:
            acumulador+=codigoEucalipto[i].replace(codigoEucalipto[i],valor[3])
        elif codigoEucalipto[i] in codigo[4]:
            acumulador+=codigoEucalipto[i].replace(codigoEucalipto[i],valor[4])
        elif codigoEucalipto[i] in codigo[5]:
            acumulador+=codigoEucalipto[i].replace(codigoEucalipto[i],valor[5])
        elif codigoEucalipto[i] in codigo[6]:
            acumulador+=codigoEucalipto[i].replace(codigoEucalipto[i],valor[6])
        elif codigoEucalipto[i] in codigo[7]:
            acumulador+=codigoEucalipto[i].replace(codigoEucalipto[i],valor[7])
        elif codigoEucalipto[i] in codigo[8]:
            acumulador+=codigoEucalipto[i].replace(codigoEucalipto[i],valor[8])
        elif codigoEucalipto[i] in codigo[9]:
            acumulador+=codigoEucalipto[i].replace(codigoEucalipto[i],valor[3])
        elif codigoEucalipto[i] in codigo[10]:
            acumulador+=codigoEucalipto[i].replace(codigoEucalipto[i],valor[0])
        elif codigoEucalipto[i] in codigo[11]:
            acumulador+=codigoEucalipto[i].replace(codigoEucalipto[i],valor[5])
        elif codigoEucalipto[i] in codigo[12]:
            acumulador+=codigoEucalipto[i].replace(codigoEucalipto[i],valor[8])
        elif codigoEucalipto[i] in codigo[13]:
            acumulador+=codigoEucalipto[i].replace(codigoEucalipto[i],valor[1])
        elif codigoEucalipto[i].isspace():
            acumulador+='°'
        else:
           acumulador+=codigoEucalipto[i] 
    return (acumulador.lower())
def opcionDecodificarCodigoEucalipto():
    """
    Funcionamiento: Recibe el código escrito por el usuario
    Entrada: Código escrito por el usuario
    Salida: Imprime la variable AuxDecodEuc y al finalizar llama al menu
    Restricción: Si la variable AuxDecodEuc retorna vacío, llama a opcionDecodificarCodigoEucalipto
    """
    decodificadorEucalipto=input('Escriba el código eucalipto a decodificar: ')
    AuxDecodEuc=opcionDecodificarCodigoEucaliptoAux(decodificadorEucalipto)
    print(AuxDecodEuc)
    if AuxDecodEuc=='':
        return opcionDecodificarCodigoEucalipto()
    pickle.dump(time.strftime("%H:%M:%S")+' '+'Eucalipto-Dec : entra('+decodificadorEucalipto+')'+',sale('+AuxDecodEuc+')',f)
    return menu()
def opcionDecodificarCodigoEucaliptoAux(decodificadorEucalipto):
    """
    Funcionamiento: Válida el código escrito por el usuario
    Entrada: decodificadorEucalipto
    Salida: Llama a la función decodificarCodigoEucalipto
    """
    if len(decodificadorEucalipto)==0:
        print('El código  eucalipto debe conter información')
        return ''
    return decodificarCodigoEucalipto(decodificadorEucalipto.upper())
def decodificarCodigoEucalipto(decodificadorEucalipto):
    """
    Funcionamiento: Decodifica el código escrito por el usuario
    Entrada: decodificadorEucalipto
    Salida: acumulador
    """
    valor=['E','U','C','A','L','I','P','T','O']
    codigo=['1','2','3','4','5','6','7','8','9']
    acumulador=''
    for i in range(len(decodificadorEucalipto)):
        if decodificadorEucalipto[i] in codigo[0]:
            acumulador+=decodificadorEucalipto[i].replace(decodificadorEucalipto[i],valor[0])
        elif decodificadorEucalipto[i] in codigo[1]:
            acumulador+=decodificadorEucalipto[i].replace(decodificadorEucalipto[i],valor[1])
        elif decodificadorEucalipto[i] in codigo[2]:
            acumulador+=decodificadorEucalipto[i].replace(decodificadorEucalipto[i],valor[2])
        elif decodificadorEucalipto[i] in codigo[3]:
            acumulador+=decodificadorEucalipto[i].replace(decodificadorEucalipto[i],valor[3])
        elif decodificadorEucalipto[i] in codigo[4]:
            acumulador+=decodificadorEucalipto[i].replace(decodificadorEucalipto[i],valor[4])
        elif decodificadorEucalipto[i] in codigo[5]:
            acumulador+=decodificadorEucalipto[i].replace(decodificadorEucalipto[i],valor[5])
        elif decodificadorEucalipto[i] in codigo[6]:
            acumulador+=decodificadorEucalipto[i].replace(decodificadorEucalipto[i],valor[6])
        elif decodificadorEucalipto[i] in codigo[7]:
            acumulador+=decodificadorEucalipto[i].replace(decodificadorEucalipto[i],valor[7])
        elif decodificadorEucalipto[i] in codigo[8]:
            acumulador+=decodificadorEucalipto[i].replace(decodificadorEucalipto[i],valor[8])
        elif decodificadorEucalipto[i].isspace():
            acumulador+=' '
        else:
           acumulador+=decodificadorEucalipto[i]
    acumulador=acumulador.replace('°',' ') 
    return (acumulador.lower())
def opcionCodificarCenitPolar():
    """
    Funcionamiento: Recibe el código escrito por el usuario
    Entrada: Código escrito por el usuario
    Salida: Imprime la variable AuxCodCen y al finalizar llama al menu
    Restricción: Si la variable AuxCodCen retorna vacío, llama a opcionCodificarCenitPolar
    """
    palabraC=input('Escriba el texto a codificar: ')
    AuxCodCen=opcionCodificarCenitPolarAux(palabraC.upper())
    print(AuxCodCen)
    if AuxCodCen=='':
        return opcionCodificarCenitPolar()
    pickle.dump(time.strftime("%H:%M:%S")+' '+'CenitPolar-Cod : entra('+palabraC+')'+',sale('+AuxCodCen+')',f)
    return menu()
def opcionCodificarCenitPolarAux(palabraC):
    """
    Funcionamiento: Válida el código escrito por el usuario
    Entrada: palabra
    Salida: Llama a la función codificarCenitPolar
    """
    if len(palabraC)==0:
        print('El texto debe conter información')
        return ''
    for i in palabraC:
        if i.isdigit():
            print('El texto no admite numeros')
            return ''
    return codificarCenitPolar(palabraC)
def codificarCenitPolar(palabraC):
    """
    Funcionamiento: Codifica el texto ingresado por el usuario
    Entrada: palabraC
    Salida: acumulador
    """
    codigoMur=["C", "E", "N", "I", "T","P", "O", "L", "A", "R"]
    remplazos=["P", "O", "L", "A", "R","C", "E", "N", "I", "T"]
    acumulador=""
    for i in range(len(palabraC)):
        if palabraC[i]==codigoMur[0]:
            acumulador+=palabraC[i].replace(palabraC[i],remplazos[0])
        elif palabraC[i]==codigoMur[1]:
            acumulador+=palabraC[i].replace(palabraC[i],remplazos[1])
        elif palabraC[i]==codigoMur[2]:
            acumulador+=palabraC[i].replace(palabraC[i],remplazos[2])
        elif palabraC[i]==codigoMur[3]:
            acumulador+=palabraC[i].replace(palabraC[i],remplazos[3])
        elif palabraC[i]==codigoMur[4]:
            acumulador+=palabraC[i].replace(palabraC[i],remplazos[4])
        elif palabraC[i]==codigoMur[5]:
            acumulador+=palabraC[i].replace(palabraC[i],remplazos[5])
        elif palabraC[i]==codigoMur[6]:
            acumulador+=palabraC[i].replace(palabraC[i],remplazos[6])
        elif palabraC[i]==codigoMur[7]:
            acumulador+=palabraC[i].replace(palabraC[i],remplazos[7])
        elif palabraC[i]==codigoMur[8]:
            acumulador+=palabraC[i].replace(palabraC[i],remplazos[8])
        elif palabraC[i]==codigoMur[9]:
            acumulador+=palabraC[i].replace(palabraC[i],remplazos[9])
        else:
            acumulador+=palabraC[i]
    acumulador=acumulador.replace(" ", "¬")
    return acumulador.lower()
def opcionDecodificarCenitPolar():
    """
    Funcionamiento: Recibe el código escrito por el usuario
    Entrada: Código escrito por el usuario
    Salida: Imprime la variable AuxDecodCen y al finalizar llama al menu
    Restricción: Si la variable AuxDecodCen retorna vacío, llama a opcionDecodificarCenitPolar
    """
    codigoCen=input('Escriba el codigo a decodificar: ')
    AuxDecodCen=opcionDecodificarCenitPolarAux(codigoCen)
    print(AuxDecodCen)
    if AuxDecodCen=='':
        return opcionDecodificarCenitPolar()
    pickle.dump(time.strftime("%H:%M:%S")+' '+'CenitPolar-Dec : entra('+codigoCen+')'+',sale('+AuxDecodCen+')',f)
    return menu()
def opcionDecodificarCenitPolarAux(codigoCen):
    """
    Funcionamiento: Válida el código escrito por el usuario
    Entrada: codigoCen
    Salida: Llama a la función decodificarCodigoMurcielago
    """
    codigoCen=codigoCen.upper()
    if len(codigoCen)==0:
        print('El texto debe conter información')
        return ''
    for i in codigoCen:
        if i.isdigit():
            print('El texto no admite numeros')
            return ''
    return decodificarCenitPolar(codigoCen)
def decodificarCenitPolar(codigoCen):
    """
    Función: Decodificar el texto ingresado por el usuario.
    Entrada: La variable "codigoCen".
    Salida: La variable "acumulador"
    """
    codigoMur=["P", "O", "L", "A", "R","C", "E", "N", "I", "T"]
    remplazos=["C", "E", "N", "I", "T","P", "O", "L", "A", "R"]
    acumulador=""
    for i in range(len(codigoCen)):
        if codigoCen[i]==codigoMur[0]:
            acumulador+=codigoCen[i].replace(codigoCen[i],remplazos[0])
        elif codigoCen[i]==codigoMur[1]:
            acumulador+=codigoCen[i].replace(codigoCen[i],remplazos[1])
        elif codigoCen[i]==codigoMur[2]:
            acumulador+=codigoCen[i].replace(codigoCen[i],remplazos[2])
        elif codigoCen[i]==codigoMur[3]:
            acumulador+=codigoCen[i].replace(codigoCen[i],remplazos[3])
        elif codigoCen[i]==codigoMur[4]:
            acumulador+=codigoCen[i].replace(codigoCen[i],remplazos[4])
        elif codigoCen[i]==codigoMur[5]:
            acumulador+=codigoCen[i].replace(codigoCen[i],remplazos[5])
        elif codigoCen[i]==codigoMur[6]:
            acumulador+=codigoCen[i].replace(codigoCen[i],remplazos[6])
        elif codigoCen[i]==codigoMur[7]:
            acumulador+=codigoCen[i].replace(codigoCen[i],remplazos[7])
        elif codigoCen[i]==codigoMur[8]:
            acumulador+=codigoCen[i].replace(codigoCen[i],remplazos[8])
        elif codigoCen[i]==codigoMur[9]:
            acumulador+=codigoCen[i].replace(codigoCen[i],remplazos[9])
        else:
            acumulador+=codigoCen[i]
    acumulador=acumulador.replace("¬", " ")    
    return (acumulador.lower())
def opcionCodificarCodigoMorse():
    """
    Funcionamiento: Recibe el código escrito por el usuario
    Entrada: Código escrito por el usuario
    Salida: Imprime la variable AuxCodMor y al finalizar llama al menu
    Restricción: Si la variable AuxCodMor retorna vacío, llama a opcionCodificarCodigoMorse
    """
    codigoMorse=input('Escriba el texto a codificar: ')
    AuxCodMor=opcionCodificarCodigoMorseAux(codigoMorse.upper())
    print(AuxCodMor)
    if AuxCodMor=='':
        return opcionCodificarCodigoMorse()
    pickle.dump(time.strftime("%H:%M:%S")+' '+'Morse-Cod : entra('+codigoMorse+')'+',sale('+AuxCodMor+')',f)
    return menu()
def opcionCodificarCodigoMorseAux(codigoMorse):
    """
    Funcionamiento: Válida el código escrito por el usuario
    Entrada: codigoMorse
    Salida: Llama a la función codificarCodigoMorse
    """
    if len(codigoMorse)==0:
        print('Lo escrito debe conter información')
        return ''
    for i in codigoMorse:
        caracteresValidos=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S',' ']
        caracteresValidos2=['T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
        totalCaracteresValidos= caracteresValidos+ caracteresValidos2
        if i not in totalCaracteresValidos:
            print('Este programa solo acepta el abecedario morse')
            return ''
    return codificarCodigoMorse(codigoMorse.upper())
def codificarCodigoMorse(codigoMorse):
    """
    Funcionamiento: Codifica el texto escrito por el usuario
    Entrada: codigoMorse
    Salida: acumulador 
    """
    codigo=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S']
    codigo2=['T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
    codigo3= codigo+codigo2
    valor=['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','—.','---']
    valor2=['.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','-----','.----']
    valor3=['..---','...--','....-','.....','-....','--...','---..','----.']
    valorTotal=valor+valor2+valor3
    acumulador=''
    simbolo=['^',' ']
    for i in range(len(codigoMorse)):
        if codigoMorse[i] in codigo3[0]:
            acumulador+=codigoMorse[i].replace(codigoMorse[i],valorTotal[0])
        elif codigoMorse[i] in codigo3[1]:
            acumulador+=codigoMorse[i].replace(codigoMorse[i],valorTotal[1])
        elif codigoMorse[i] in codigo3[2]:
            acumulador+=codigoMorse[i].replace(codigoMorse[i],valorTotal[2])
        elif codigoMorse[i] in codigo3[3]:
            acumulador+=codigoMorse[i].replace(codigoMorse[i],valorTotal[3])
        elif codigoMorse[i] in codigo3[4]:
            acumulador+=codigoMorse[i].replace(codigoMorse[i],valorTotal[4])
        elif codigoMorse[i] in codigo3[5]:
            acumulador+=codigoMorse[i].replace(codigoMorse[i],valorTotal[5])
        elif codigoMorse[i] in codigo3[6]:
            acumulador+=codigoMorse[i].replace(codigoMorse[i],valorTotal[6])
        elif codigoMorse[i] in codigo3[7]:
            acumulador+=codigoMorse[i].replace(codigoMorse[i],valorTotal[7])
        elif codigoMorse[i] in codigo3[8]:
            acumulador+=codigoMorse[i].replace(codigoMorse[i],valorTotal[8])
        elif codigoMorse[i] in codigo3[9]:
            acumulador+=codigoMorse[i].replace(codigoMorse[i],valorTotal[9])
        elif codigoMorse[i] in codigo3[10]:
            acumulador+=codigoMorse[i].replace(codigoMorse[i],valorTotal[10])
        elif codigoMorse[i] in codigo3[11]:
            acumulador+=codigoMorse[i].replace(codigoMorse[i],valorTotal[11])
        elif codigoMorse[i] in codigo3[12]:
            acumulador+=codigoMorse[i].replace(codigoMorse[i],valorTotal[12])
        elif codigoMorse[i] in codigo3[13]:
            acumulador+=codigoMorse[i].replace(codigoMorse[i],valorTotal[13])
        elif codigoMorse[i] in codigo3[14]:
            acumulador+=codigoMorse[i].replace(codigoMorse[i],valorTotal[14])
        elif codigoMorse[i] in codigo3[15]:
            acumulador+=codigoMorse[i].replace(codigoMorse[i],valorTotal[15])
        elif codigoMorse[i] in codigo3[16]:
            acumulador+=codigoMorse[i].replace(codigoMorse[i],valorTotal[16])
        elif codigoMorse[i] in codigo3[17]:
            acumulador+=codigoMorse[i].replace(codigoMorse[i],valorTotal[17])
        elif codigoMorse[i] in codigo3[18]:
            acumulador+=codigoMorse[i].replace(codigoMorse[i],valorTotal[18])
        elif codigoMorse[i] in codigo3[19]:
            acumulador+=codigoMorse[i].replace(codigoMorse[i],valorTotal[19])
        elif codigoMorse[i] in codigo3[20]:
            acumulador+=codigoMorse[i].replace(codigoMorse[i],valorTotal[20])
        elif codigoMorse[i] in codigo3[21]:
            acumulador+=codigoMorse[i].replace(codigoMorse[i],valorTotal[21])
        elif codigoMorse[i] in codigo3[22]:
            acumulador+=codigoMorse[i].replace(codigoMorse[i],valorTotal[22])
        elif codigoMorse[i] in codigo3[23]:
            acumulador+=codigoMorse[i].replace(codigoMorse[i],valorTotal[23])
        elif codigoMorse[i] in codigo3[24]:
            acumulador+=codigoMorse[i].replace(codigoMorse[i],valorTotal[24])
        elif codigoMorse[i] in codigo3[25]:
            acumulador+=codigoMorse[i].replace(codigoMorse[i],valorTotal[25])
        elif codigoMorse[i] in codigo3[26]:
            acumulador+=codigoMorse[i].replace(codigoMorse[i],valorTotal[26])
        elif codigoMorse[i] in codigo3[27]:
            acumulador+=codigoMorse[i].replace(codigoMorse[i],valorTotal[27])
        elif codigoMorse[i] in codigo3[28]:
            acumulador+=codigoMorse[i].replace(codigoMorse[i],valorTotal[28])
        elif codigoMorse[i] in codigo3[29]:
            acumulador+=codigoMorse[i].replace(codigoMorse[i],valorTotal[29])
        elif codigoMorse[i] in codigo3[30]:
            acumulador+=codigoMorse[i].replace(codigoMorse[i],valorTotal[30])
        elif codigoMorse[i] in codigo3[31]:
            acumulador+=codigoMorse[i].replace(codigoMorse[i],valorTotal[31])
        elif codigoMorse[i] in codigo3[32]:
            acumulador+=codigoMorse[i].replace(codigoMorse[i],valorTotal[32])
        elif codigoMorse[i] in codigo3[33]:
            acumulador+=codigoMorse[i].replace(codigoMorse[i],valorTotal[33])
        elif codigoMorse[i] in codigo3[34]:
            acumulador+=codigoMorse[i].replace(codigoMorse[i],valorTotal[34])
        elif codigoMorse[i] in codigo3[35]:
            acumulador+=codigoMorse[i].replace(codigoMorse[i],valorTotal[35])           
        elif codigoMorse[i].isspace():
            acumulador+='|'
        if len(codigoMorse)-1!=i and codigoMorse[i]!=simbolo[1]:
            acumulador+=simbolo[0]
    return (acumulador)
def opcionDecodificarCodigoMorse():
    """
    Funcionamiento: Recibe el código escrito por el usuario
    Entrada: Código escrito por el usuario
    Salida: Imprime la variable AuxDecodMor y al finalizar llama al menu
    Restricción: Si la variable AuxDecodMor retorna vacío, llama a opcionDecodificarCodigoMorse
    """
    decodificadorMorse=input('Escriba el código morse a decodificar: ')
    AuxDecodMor=opcionDecodificarCodigoMorseAux(decodificadorMorse)
    print(AuxDecodMor)
    if AuxDecodMor=='':
        return opcionDecodificarCodigoMorse()
    pickle.dump(time.strftime("%H:%M:%S")+' '+'Morse-Dec : entra('+decodificadorMorse+')'+',sale('+AuxDecodMor+')',f)
    return menu()
def opcionDecodificarCodigoMorseAux(decodificadorMorse):
    """
    Funcionamiento: Válida el código escrito por el usuario
    Entrada: decodificadorMorse
    Salida: Llama a la función decodificarCodigoMorse
    """
    caracteresValidos=['-',"-.",'^','|','.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','---']
    caracteresValidos2=['.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','-----','.----']
    caracteresValidos3=['..---','...--','....-','.....','-....','--...','---..','----.']
    totalCaracteresValidos=caracteresValidos+ caracteresValidos2+caracteresValidos3
    if len(decodificadorMorse)==0:
        print('El código morse debe conter información')
        return ''
    for i in decodificadorMorse.split('^'):
        if i in totalCaracteresValidos:
            return decodificarCodigoMorse(decodificadorMorse)
        print('Este programa solo acepta código morse')
        return ''            
def decodificarCodigoMorse(codigoMorse):
    """
    Funcionamiento: Decodifica el código escrito por el usuario
    Entrada: codigoMorse
    Salida: acumulador 
    """
    valor=['A','D','C','B','E','U','M','H','I','O','K','L','G','N','J','P','Q','R','S']
    valor2=['T','F','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9',' ']
    valorTotal=valor+valor2
    codigo=('.-','-..','-.-.','-...','.','..-','--','....','..','---','-.-','.-..','--.','-.','.---')
    codigo2=('.--.','--.-','.-.','...','-','..-.','...-','.--','-..-','-.--','--..','-----','.----')
    codigo3=('..---','...--','....-','.....','-....','--...','---..','----.','')
    codigo4= codigo+codigo2+codigo3
    acumulador=''
    j=''
    j=codigoMorse.split('^')
    for i in range(len(j)):
        #Agrega un espacio y cambia el valor posicional de j[i] por uno nuevo en el cual se le elimina el '|'
        if '|' in j[i]:
            acumulador+=' '
            j[i]=j[i].replace('|','')
        if j[i] == codigo4[0]:
            acumulador+=j[i].replace(j[i],valorTotal[0])
        elif j[i] ==codigo4[1]:
            acumulador+=j[i].replace(j[i],valorTotal[1])
        elif j[i] == codigo4[2]:
            acumulador+=j[i].replace(j[i],valorTotal[2])
        elif j[i] == codigo4[3]:
            acumulador+=j[i].replace(j[i],valorTotal[3])
        elif j[i] == codigo4[4]:
            acumulador+=j[i].replace(j[i],valorTotal[4])
        elif j[i] == codigo4[5]:
            acumulador+=j[i].replace(j[i],valorTotal[5])
        elif j[i] == codigo4[6]:
            acumulador+=j[i].replace(j[i],valorTotal[6])
        elif j[i] == codigo4[7]:
            acumulador+=j[i].replace(j[i],valorTotal[7])
        elif j[i] == codigo4[8]:
            acumulador+=j[i].replace(j[i],valorTotal[8])
        elif j[i] == codigo4[9]:
            acumulador+=j[i].replace(j[i],valorTotal[9])
        elif j[i] == codigo4[10]:
            acumulador+=j[i].replace(j[i],valorTotal[10])
        elif j[i] == codigo4[11]:
            acumulador+=j[i].replace(j[i],valorTotal[11])
        elif j[i] == codigo4[12]:
            acumulador+=j[i].replace(j[i],valorTotal[12])
        elif j[i] == codigo4[13]:
            acumulador+=j[i].replace(j[i],valorTotal[13])
        elif j[i] == codigo4[14]:
            acumulador+=j[i].replace(j[i],valorTotal[14])
        elif j[i] == codigo4[15]:
            acumulador+=j[i].replace(j[i],valorTotal[15])
        elif j[i] == codigo4[16]:
            acumulador+=j[i].replace(j[i],valorTotal[16])
        elif j[i] == codigo4[17]:
            acumulador+=j[i].replace(j[i],valorTotal[17])
        elif j[i] == codigo4[18]:
            acumulador+=j[i].replace(j[i],valorTotal[18])
        elif j[i] == codigo4[19]:
            acumulador+=j[i].replace(j[i],valorTotal[19])
        elif j[i] == codigo4[20]:
            acumulador+=j[i].replace(j[i],valorTotal[20])
        elif j[i] == codigo4[21]:
            acumulador+=j[i].replace(j[i],valorTotal[21])
        elif j[i] == codigo4[22]:
            acumulador+=j[i].replace(j[i],valorTotal[22])
        elif j[i] == codigo4[23]:
            acumulador+=j[i].replace(j[i],valorTotal[23])
        elif j[i] == codigo4[24]:
            acumulador+=j[i].replace(j[i],valorTotal[24])
        elif j[i] == codigo4[25]:
            acumulador+=j[i].replace(j[i],valorTotal[25])
        elif j[i] == codigo4[26]:
            acumulador+=j[i].replace(j[i],valorTotal[26])
        elif j[i] == codigo4[27]:
            acumulador+=j[i].replace(j[i],valorTotal[27])
        elif j[i] == codigo4[28]:
            acumulador+=j[i].replace(j[i],valorTotal[28])
        elif j[i] == codigo4[29]:
            acumulador+=j[i].replace(j[i],valorTotal[29])
        elif j[i] == codigo4[30]:
            acumulador+=j[i].replace(j[i],valorTotal[30])
        elif j[i] == codigo4[31]:
            acumulador+=j[i].replace(j[i],valorTotal[31])
        elif j[i] == codigo4[32]:
            acumulador+=j[i].replace(j[i],valorTotal[32])
        elif j[i] == codigo4[33]:
            acumulador+=j[i].replace(j[i],valorTotal[33])
        elif j[i] == codigo4[34]:
            acumulador+=j[i].replace(j[i],valorTotal[34])
        elif j[i] == codigo4[35]:
            acumulador+=j[i].replace(j[i],valorTotal[35])
    return (acumulador.lower())
def opcionCodificarCodigoSufamelico():
    """
    Funcionamiento: Recibe el código escrito por el usuario
    Entrada: Código escrito por el usuario
    Salida: Imprime la variable AuxCodSuf y al finalizar llama al menu
    Restricción: Si la variable AuxCodSuf retorna vacío, llama a opcionCodificarCodigoSufamelico
    """
    palabraS=input('Escriba el texto a codificar: ')
    AuxCodSuf=opcionCodificarCodigoSufamelicoAux(palabraS.upper())
    print(AuxCodSuf)
    if AuxCodSuf=='':
        return opcionCodificarCodigoSufamelico()
    pickle.dump(time.strftime("%H:%M:%S")+' '+'Sulfamelico-Cod : entra('+palabraS+')'+',sale('+AuxCodSuf+')',f)
    return menu()
def opcionCodificarCodigoSufamelicoAux(palabraS):
    """
    Funcionamiento: Válida el código escrito por el usuario
    Entrada: palabraS
    Salida: Llama a la función codificarSufamelico
    """
    if len(palabraS)==0:
        print('Lo escrito debe contener información')
        return ''
    for i in palabraS:
        if i.isdigit():
            print('El texto no puede llevar números')
            return ''
    return codificarSufamelico(palabraS)
def codificarSufamelico(palabraS):
    """
    Función: Codifica el texto ingresado por el usuario.
    Entrada: palabraS
    Salida: acumulador
    """
    codigoMur=["S", "U", "F", "A", "M", "E", "L", "I", "C", "O"]
    remplazos=["O", "C", "I", "L", "E", "M", "A", "F", "U", "S"]
    acumulador=""
    for i in range(len(palabraS)):
        if palabraS[i]==codigoMur[0]:
            acumulador+=palabraS[i].replace(palabraS[i],remplazos[8])
        elif palabraS[i]==codigoMur[1]:
            acumulador+=palabraS[i].replace(palabraS[i],remplazos[9])
        elif palabraS[i]==codigoMur[2]:
            acumulador+=palabraS[i].replace(palabraS[i],remplazos[6])
        elif palabraS[i]==codigoMur[3]:
            acumulador+=palabraS[i].replace(palabraS[i],remplazos[7])
        elif palabraS[i]==codigoMur[4]:
            acumulador+=palabraS[i].replace(palabraS[i],remplazos[4])
        elif palabraS[i]==codigoMur[5]:
            acumulador+=palabraS[i].replace(palabraS[i],remplazos[5])
        elif palabraS[i]==codigoMur[6]:
            acumulador+=palabraS[i].replace(palabraS[i],remplazos[2])
        elif palabraS[i]==codigoMur[7]:
            acumulador+=palabraS[i].replace(palabraS[i],remplazos[3])
        elif palabraS[i]==codigoMur[8]:
            acumulador+=palabraS[i].replace(palabraS[i],remplazos[0])
        elif palabraS[i]==codigoMur[9]:
            acumulador+=palabraS[i].replace(palabraS[i],remplazos[1])
        else:
            acumulador+=palabraS[i]
    return (acumulador.lower())
def opcionDecodificarCodigoSulfamelico():
    """
    Funcionamiento: Recibe el código escrito por el usuario
    Entrada: Código escrito por el usuario
    Salida: Imprime la variable AuxDecodSuf y al finalizar llama al menu
    Restricción: Si la variable AuxDecodSuf retorna vacío, llama a opcionDecodificarCodigoSulfamelico
    """
    codigoSulfa=input('Ingrese el código a decodificar: ')
    AuxDecodSuf=opcionDecodificarCodigoSulfamelicoAux(codigoSulfa.upper())
    print(AuxDecodSuf)
    if AuxDecodSuf=='':
        return opcionDecodificarCodigoSulfamelico()
    pickle.dump(time.strftime("%H:%M:%S")+' '+'Sulfamelico-Dec : entra('+codigoSulfa+')'+',sale('+AuxDecodSuf+')',f)
    return menu()
def opcionDecodificarCodigoSulfamelicoAux(codigoSulfa):
    """
    Funcionamiento: Válida el código escrito por el usuario
    Entrada: palabraS
    Salida: Llama a la función decodificarSufamelico
    """
    if len(codigoSulfa)==0:
        print('El código debe contener información')
        return ''
    for i in codigoSulfa:
        if i .isdigit():
            print('El código no puede llevar números')
            return ''
    return decodificarSufamelico(codigoSulfa)
def decodificarSufamelico(codigoSulfa):
    """
    Función: Codifica el texto ingresado por el usuario.
    Entrada: codigoSulfa
    Salida: acumulador
    """
    codigoMur=["U", "S", "A", "F", "E", "M", "I", "L", "O", "C"]
    remplazos=["S", "U", "F", "A", "M", "E", "L", "I", "C", "O"]
    acumulador=""
    for i in range(len(codigoSulfa)):
        if codigoSulfa[i]==codigoMur[0]:
            acumulador+=codigoSulfa[i].replace(codigoSulfa[i],remplazos[0])
        elif codigoSulfa[i]==codigoMur[1]:
            acumulador+=codigoSulfa[i].replace(codigoSulfa[i],remplazos[1])
        elif codigoSulfa[i]==codigoMur[2]:
            acumulador+=codigoSulfa[i].replace(codigoSulfa[i],remplazos[2])
        elif codigoSulfa[i]==codigoMur[3]:
            acumulador+=codigoSulfa[i].replace(codigoSulfa[i],remplazos[3])
        elif codigoSulfa[i]==codigoMur[4]:
            acumulador+=codigoSulfa[i].replace(codigoSulfa[i],remplazos[4])
        elif codigoSulfa[i]==codigoMur[5]:
            acumulador+=codigoSulfa[i].replace(codigoSulfa[i],remplazos[5])
        elif codigoSulfa[i]==codigoMur[6]:
            acumulador+=codigoSulfa[i].replace(codigoSulfa[i],remplazos[6])
        elif codigoSulfa[i]==codigoMur[7]:
            acumulador+=codigoSulfa[i].replace(codigoSulfa[i],remplazos[7])
        elif codigoSulfa[i]==codigoMur[8]:
            acumulador+=codigoSulfa[i].replace(codigoSulfa[i],remplazos[8])
        elif codigoSulfa[i]==codigoMur[9]:
            acumulador+=codigoSulfa[i].replace(codigoSulfa[i],remplazos[9])
        else:
            acumulador+=codigoSulfa[i]
    return (acumulador.lower())
def opcionDeletreo():
    """
    Funcionamiento: Recibe el código escrito por el usuario
    Entrada: Código escrito por el usuario
    Salida: Imprime la variable AuxCodDel y al finalizar llama al menu
    Restricción: Si la variable AuxCodDel retorna vacío, llama a opcionDeletreo
    """
    palabraD=input('Escriba el texto a codificar: ')
    AuxCodDel=opcionDeletreoAux(palabraD.upper())
    print(AuxCodDel)
    if AuxCodDel=='':
        return opcionDeletreo()
    pickle.dump(time.strftime("%H:%M:%S")+' '+'Deletreo-Cod : entra('+palabraD+')'+',sale('+AuxCodDel+')',f)
    return menu()
def opcionDeletreoAux(palabraD):
    """
    Funcionamiento: Válida el texto escrito por el usuario
    Entrada: palabraD
    Salida: Llama a la función codificarADeletreo
    Nota: Los caracteres especiales no son tomados en cuenta 
    """
    caracteresValidos=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    if len(palabraD)==0:
        print('La palabra debe contener información')
        return opcionDeletreo()
    for i in palabraD:
        if i== ' ':
            print('Solo se aceptan palabras o letras, no frases')
            return ''
    for j in palabraD:
        if j in caracteresValidos:
            return codificarADeletreo(palabraD)  
        return ('El texto ingresado es inválido')
    return ''
def codificarADeletreo(palabraD):
    """
    Funcionamiento: Codifica el texto escrito por el usuario
    Entrada: palabraD
    Salida: acumulador
    """
    abecedario=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] 
    acumulador=''
    simbolo=['~',' ']
    simbolo2=0
    deletreo=['Alfa','Bravo','Charlie','Delta','Echo','Foxtrot','Golf','Hotel','India','Juliet','Kilo','Lima','Mike','November','Oscar','Papa','Quebec','Romeo','Sierra','Tango','Uniform','Victor','Whisky','XRay','Yanquie','Zulú']
    for i in palabraD:
        if i in abecedario[0]:
            acumulador+=i.replace(i,deletreo[0])
        elif i in abecedario[1]:
            acumulador+=i.replace(i,deletreo[1])
        elif i in abecedario[2]:
            acumulador+=i.replace(i,deletreo[2])
        elif i in abecedario[3]:
            acumulador+=i.replace(i,deletreo[3])
        elif i in abecedario[4]:
            acumulador+=i.replace(i,deletreo[4])
        elif i in abecedario[5]:
            acumulador+=i.replace(i,deletreo[5])
        elif i in abecedario[6]:
            acumulador+=i.replace(i,deletreo[6])
        elif i in abecedario[7]:
            acumulador+=i.replace(i,deletreo[7])
        elif i in abecedario[8]:
            acumulador+=i.replace(i,deletreo[8])
        elif i in abecedario[9]:
            acumulador+=i.replace(i,deletreo[9])
        elif i in abecedario[10]:
            acumulador+=i.replace(i,deletreo[10])
        elif i in abecedario[11]:
            acumulador+=i.replace(i,deletreo[11])
        elif i in abecedario[12]:
            acumulador+=i.replace(i,deletreo[12])
        elif i in abecedario[13]:
            acumulador+=i.replace(i,deletreo[13])
        elif i in abecedario[14]:
            acumulador+=i.replace(i,deletreo[14])
        elif i in abecedario[15]:
            acumulador+=i.replace(i,deletreo[15])
        elif i in abecedario[16]:
            acumulador+=i.replace(i,deletreo[16])
        elif i in abecedario[17]:
            acumulador+=i.replace(i,deletreo[17])
        elif i in abecedario[18]:
            acumulador+=i.replace(i,deletreo[18])
        elif i in abecedario[19]:
            acumulador+=i.replace(i,deletreo[19])
        elif i in abecedario[20]:
            acumulador+=i.replace(i,deletreo[20])
        elif i in abecedario[21]:
            acumulador+=i.replace(i,deletreo[21])
        elif i in abecedario[22]:
            acumulador+=i.replace(i,deletreo[22])
        elif i in abecedario[23]:
            acumulador+=i.replace(i,deletreo[23])
        elif i in abecedario[24]:
            acumulador+=i.replace(i,deletreo[24])
        elif i in abecedario[25]:
            acumulador+=i.replace(i,deletreo[25])
        if len(palabraD)-1!=simbolo2:
            acumulador+=simbolo[0]
        simbolo2+=1
    return (acumulador.lower())
def opcionDecodificarDeletreo():
    """
    Funcionamiento: Recibe el código escrito por el usuario
    Entrada: Código escrito por el usuario
    Salida: Imprime la variable AuxDecodDel y al finalizar llama al menu
    Restricción: Si la variable AuxDecodDel retorna vacío, llama a opcionDecodificarDeletreo
    """
    decodificarD=input('Escriba el código a decodificar: ')
    AuxDecodDel=opcionDecodificarDeletreoAux(decodificarD.title())
    print(AuxDecodDel)
    if AuxDecodDel=='':
        return opcionDecodificarDeletreo()
    pickle.dump(time.strftime("%H:%M:%S")+' '+'Deletreo-Dec : entra('+decodificarD+')'+',sale('+AuxDecodDel+')',f)
    return menu()
def opcionDecodificarDeletreoAux(decodificar):
    """
    Funcionamiento: Válida el texto escrito por el usuario
    Entrada: decodificar
    Salida: Llama a la función decodificarADeletreo(palabra)
    """
    caracteresValidos=['Alfa','Bravo','Charlie','Delta','Echo','Foxtrot','Golf','Hotel','India','Juliet','Kilo','Lima','Mike','November','Oscar','Papa','Quebec','Romeo','Sierra','Tango','Uniform','Victor','Whisky','XRay','Yanquie','Zulú','~']
    if len(decodificar)==0:
        print('El deletreo debe contener información')
        return ''
    if len(decodificar) >=4:
        for i in decodificar:
            if i.isdigit():
                print('El deletreo no debe contener números')
                return ''
        for j in decodificar.split('~'):
            if j in caracteresValidos:
                return decodificarADeletreo(decodificar)
            else:
                print('El código escrito es inválido') 
                return ''
    print('El código debe ser mayor a 3 caracteres')
    return ''
def decodificarADeletreo(palabra):
    """
    Funcionamiento: Decodifica el código escrito por el usuario
    Entrada: palabra
    Salida: acumulador
    """
    deletreo =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] 
    acumulador=''
    abecedario=['Alfa','Bravo','Charlie','Delta','Echo','Foxtrot','Golf','Hotel','India','Juliet','Kilo','Lima','Mike','November','Oscar','Papa','Quebec','Romeo','Sierra','Tango','Uniform','Victor','Whisky','XRay','Yanquie','Zulú']
    for i in palabra.split('~'):
        if i in abecedario[0]:
            acumulador+=palabra.replace(palabra,deletreo[0])
        elif i in abecedario[1]:
            acumulador+=palabra.replace(palabra,deletreo[1])
        elif i in abecedario[2]:
            acumulador+=palabra.replace(palabra,deletreo[2])
        elif i in abecedario[3]:
            acumulador+=palabra.replace(palabra,deletreo[3])
        elif i in abecedario[4]:
            acumulador+=palabra.replace(palabra,deletreo[4])
        elif i in abecedario[5]:
            acumulador+=palabra.replace(palabra,deletreo[5])
        elif i in abecedario[6]:
            acumulador+=palabra.replace(palabra,deletreo[6])
        elif i in abecedario[7]:
            acumulador+=palabra.replace(palabra,deletreo[7])
        elif i in abecedario[8]:
            acumulador+=palabra.replace(palabra,deletreo[8])
        elif i in abecedario[9]:
            acumulador+=palabra.replace(palabra,deletreo[9])
        elif i in abecedario[10]:
            acumulador+=palabra.replace(palabra,deletreo[10])
        elif i in abecedario[11]:
            acumulador+=palabra.replace(palabra,deletreo[11])
        elif i in abecedario[12]:
            acumulador+=palabra.replace(palabra,deletreo[12])
        elif i in abecedario[13]:
            acumulador+=palabra.replace(palabra,deletreo[13])
        elif i in abecedario[14]:
            acumulador+=palabra.replace(palabra,deletreo[14])
        elif i in abecedario[15]:
            acumulador+=palabra.replace(palabra,deletreo[15])
        elif i in abecedario[16]:
            acumulador+=palabra.replace(palabra,deletreo[16])
        elif i in abecedario[17]:
            acumulador+=palabra.replace(palabra,deletreo[17])
        elif i in abecedario[18]:
            acumulador+=palabra.replace(palabra,deletreo[18])
        elif i in abecedario[19]:
            acumulador+=palabra.replace(palabra,deletreo[19])
        elif i in abecedario[20]:
            acumulador+=palabra.replace(palabra,deletreo[20])
        elif i in abecedario[21]:
            acumulador+=palabra.replace(palabra,deletreo[21])
        elif i in abecedario[22]:
            acumulador+=palabra.replace(palabra,deletreo[22])
        elif i in abecedario[23]:
            acumulador+=palabra.replace(palabra,deletreo[23])
        elif i in abecedario[24]:
            acumulador+=palabra.replace(palabra,deletreo[24])
        elif i in abecedario[25]:
            acumulador+=palabra.replace(palabra,deletreo[25])
    return (acumulador.lower())
def menu():
    """
    Funcionamiento: Recibe el una opción por el usuario
    Entrada: Opción escrita por el usuario
    Salida: Llama a una función, según la opción indicada por el usuario 
    """
    try:
        print('\n***********************\n0-Teminar el programa\n1-Codificar texto a código murcielago\n2-Decoficar código murcielago a texto\n\
3-Codificar texto a código eucalipto\n4-Decodificar código eucalipto a texto\n5-Codificar texto a código cenit polar\n\
6-Decodificar código cenit polar a texto\n7-Codificar texto a código morse\n8-Decodificar de código morse a texto\n\
9-Codificar texto a código sufamelico\n10-Decodificar código sufamelico a texto\n11-Codificar texto a código deletreo\n\
12-Decodificar código deletreo a texto')
        opcion=int(input('Escoja una opción: '))
        if opcion>=0 or opcion<=12:
            if opcion==0:
                return ''
            elif opcion==1:
                return opcionCodificarCodigoMurcielago()
            elif opcion==2:
                return opcionDecodificarCodigoMurcielago()
            elif opcion==3:
                return opcionCodificarCodigoEucalipto()
            elif opcion==4:
                return opcionDecodificarCodigoEucalipto()
            elif opcion==5:
                return opcionCodificarCenitPolar()
            elif opcion==6:
                return opcionDecodificarCenitPolar()
            elif opcion==7:
                return opcionCodificarCodigoMorse()
            elif opcion==8:
                return opcionDecodificarCodigoMorse()
            elif opcion==9:
                return opcionCodificarCodigoSufamelico()
            elif opcion==10:
                return opcionDecodificarCodigoSulfamelico()
            elif opcion==11:
                return opcionDeletreo()
            elif opcion==12:
                return opcionDecodificarDeletreo()
        else:
            print('Debe ingresar una opción válida')
            return menu()
        if opcion<0 or opcion==-0:
            print('Debe ingresar una opción válida')
            return menu()
    except ValueError:
        print('Debe ingresar una opción válida')
        return menu()
    return ''
#Programa principal
menu()
#Cierre de la bitacora
f.close()
print('\n************\nBitácora')
f=open('Bitacora.dat','rb')
while True:
    try:
        x=pickle.load(f)
        print(x)
    except EOFError:
        break
f.close()

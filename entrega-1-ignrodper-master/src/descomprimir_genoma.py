def descomprime_fichero(origen, destino):
    """función que descomprime un fichero de nucleótidos comprimido y guarda el resultado
    en otro fichero
    Args:
        origen (str): ruta hacia el fichero comprimido
        destino (str): ruta hacia el fichero donde se guardarán los datos originales
    """
    import os

    with open(origen,'r', encoding='utf-8') as f:      #abre el fichero comprimido
        letras=('A','G','C','T')                       #declaracion de las letras de mi fichero
        inf=range(1000)                                #crea una lista de numeros
        n=[str(x) for x in inf]                        #cambia la lista de numeros a string para comparar con la de mi txt
        a=0                                            #declaracion de variable para guardar el num anterior a mi letra
            
        if os.path.exists(destino):                    #chekea si el fichero destino existe 
            os.remove(destino)                         #elimina el fichero para q no se solape 
        descom = open(destino, 'w')                    #abre el fichero nuevo

        while True:                                    #recorre fichero comprimido
            i=f.read(1)                                #lee caracter por caracter
            if i in n:                                 #comprueba si i es un numero
                if i in n and a in n:                  #comprueba si i es un numero de mas de 1 cifra
                    a= a+i                             #guarda el numero en a para despues multiplicar 
                else:                                  #numero de 1 cifra
                    a= i                                    
                    
            elif i in letras:                          #comprueba si i es una letra
                if a in n or a in n:                   #compruba si hay q multiplicar la letra por el num anterior
                    i = i * int(a)                     #multiplica i (q es una letra) por a (numero anterior,cambia a int para mult) 
                    descom.write(i)                    #guarda la letra multiplicada en el fichero
                else:                                  #si no hay q multiplicar     
                    descom.write(i)                    #guarda la letra en el fichero
                a=0                                    #forma de eliminar el num anterior guardado
            elif i=='\n':                              #por cada salto de linea 
                descom.write('\n')                     #añade un salto de linea al fichero nuevo
            elif not i:                                #acaba el programa cuando no hay mas letras
                break
        descom.close()                                 #se cierra el fichero con el resultado descomprimido



  
def descomprime(txt):
    """función auxiliar que descomprime una línea del fichero comprimido y la devuelve en su formato original

    Args:
        txt (str): línea de texto que representa una secuencia de nucleótidos en formato comprimido

    Returns:
        str: secuencia de nucleótidos
    """
    a=0
    letras=('A','G','C','T')
    inf=range(1000)                                    
    n=[str(x) for x in inf]                                 

    descom=''                           #guarda en una variable
    
    for i in txt:                       #recorre la linea de txt a descomprimir
        if i in n:                      #utilizo el codigo de la funcion anterior
            if i in n and a in n:       #tambien se podria guardar el codigo de descomprimir 
                a= a+i                  #en una funcion para poder llamarla y no tener q copiar codigo
            else:                                           
                a= i                                        
                
        elif i in letras or a in n:                                   
            if a in n:                                    
                i = i * int(a)                              
                descom=descom + i       #guarda la letra multiplicada en la variable a devolver
            else:                                                        
                descom=descom + i 
            a=0                                             
    
    return descom
    

def check_Ok(descomprimido, original):
    """función que comprueba si el fichero generado por nosotros coincide con el original

    Args:
        descomprimido (str): ruta hacia el fichero descomprimido por nosotros
        original (str): ruta hacia el fichero original

    Returns:
        bool: Devuelve True si el fichero descomprimido coincide con el original
    """
    ok=True
    fd=open(descomprimido, encoding='utf-8')
    fo=open(original, encoding='utf-8')
    for linea1,linea2 in zip(fd,fo):
        ok=linea1==linea2
        if not ok:
            break
    fd.close()
    fo.close()
    return ok

######################################### Test ################################################
if __name__ == '__main__':
    '''
    Realice las siguientes pruebas:
    1.- descomprima el fichero 'sacCer3cmp.txt' y guardelo en el fichero 'sacCer3descmp.txt' 
        (ambos en la ruta de la carpeta 'data')
    2.- Compruebe que el algoritmo funciona usando el método 'ckeck_Ok', que toma como parámetros
        la ruta hacia el fichero que usted ha generado ('sacCer3descmp.txt'), y la ruta hacia 
        el fichero original ('sacCer3.txt')
    '''
    descomprime_fichero('data\sacCer3cmp.txt', 'data\sacCer3descmp.txt')
    check_Ok('data\sacCer3descmp.txt', 'data\sacCer3cmp.txt')

from tkinter.constants import NUMERIC
from PIL import Image
import tkinter as tk
import random as r
import unidecode as un
def clicGenerar():
    #ALMACENAR LA HOJA DE LIBRETA EN UNA VARIABLE
        img =Image.open("hojaLibreta.png")
        img.resize((300,500))
        #Posicion inicial 
        x = 70
        y = 225
        numRenglones = 0
        numImagen = 1
        texto = un.unidecode(obtenerTexto())
        
        for i in range(0,len(texto)):
            #print("Caracter "+texto[i])
            if(texto[i] == '\n'):
                if numRenglones == 4:
                    y+= 75
                elif numRenglones == 8:
                    y+= 75 
                elif numRenglones == 11:
                    y+= 75
                elif numRenglones == 15:
                    y+= 65
                elif numRenglones == 19:
                    y+= 75
                elif numRenglones == 21:
                    y+= 75
                elif numRenglones == 24:
                    y+= 75
                else:
                    y+= 100
                x = 70
                numRenglones += 1
                if numRenglones == 28:
                   numRenglones = 0
                   x = 65
                   y = 225
                   img.save("Hoja"+str(numImagen)+".png")
                   numImagen += 1
                   img =Image.open("hojaLibreta.png")
                continue
            
            if(texto[i] != ' ' and texto[i] != '\n' ):
                carpeta = "textoMayusculaJorge"
                if(texto[i].islower() or texto[i] in ['?','.',',']):
                    carpeta = "textoMinusculaJorge"
                if(texto[i] in ['1','2','3','4','5','6','7','8','9','0']):         
                    carpeta = "NumerosJorge"
                    nomArchivo = texto[i]
                if(carpeta == "textoMinusculaJorge"):
                    numR = str(r.randint(1,5))
                    nomArchivo = texto[i]+numR
                if(carpeta == "textoMayusculaJorge"):
                    numR = str(r.randint(1,2))
                    nomArchivo = texto[i]+numR
                if(texto[i] == '.'):
                    nomArchivo = "punto"
                elif(texto[i] == ','):
                    nomArchivo = "coma"
                elif(texto[i] == "?"):
                    nomArchivo = "signoInterrogacion"
                elif(texto[i] == ":"):
                    nomArchivo = "dosPuntos"
                elif(texto[i] == "("):
                    nomArchivo = "("
                elif(texto[i] ==  ")"):
                    nomArchivo = ")"
                elif(texto[i] == ":"):
                    nomArchivo = "dosPuntos"
                imgCar = Image.open("./"+carpeta+"/J"+nomArchivo+".png")
                imgCar = imgCar.resize((50,50))
                if(carpeta == "textoMinusculaJorge"):
                    if(texto[i] in ['.',',']):
                        imgCar = imgCar.resize((20,20))
                        vr = y+40;
                    elif(texto[i] in ['i']):
                        imgCar = imgCar.resize((20,40))
                        vr = y+10
                    else: 
                        imgCar = imgCar.resize((40,40))
                        vr= y+10#r.randint(y+5,y+20)
                elif texto[i] == ':':
                    imgCar = imgCar.resize((20,40))
                else:
                    vr = r.randint(y+8,y+12)#y+10
               
                
                #Pegar la imagen
                img.paste(imgCar,(x,vr),mask = imgCar)
            #Espacio entre letras
            if(texto[i] == "i"):
                x += r.randint(10,30)
           # elif)
            elif(i != len(texto)-1 and texto[i+1] == ":"):
                x += r.randint(50,60)
            else:
                x += r.randint(25,50)
            #Salto de Renglon
           # x > 1850 or 
            if  not revisarPalabra(i,x):
                if numRenglones == 4:
                    y+= 75
                elif numRenglones == 8:
                    y+= 75
                elif numRenglones == 11:
                    y+= 75
                elif numRenglones == 15:
                    y+= 65
                elif numRenglones == 19:
                    y+= 75
                elif numRenglones == 21:
                    y+= 75
                elif numRenglones == 24:
                    y+= 75
                else:
                    y+= 100
                x = 70
                numRenglones += 1
            if numRenglones == 28:
                numRenglones = 0
                x = 70
                y = 225
                img.save("Hoja"+str(numImagen)+".png")
                numImagen += 1
                img =Image.open("hojaLibreta.png")
                
        #Guardar la imagen
        img.save("Hoja"+str(numImagen)+".png")

def obtenerTexto():
    return str(textArea.get(index1= "1.0",index2='end-1c'))

def revisarPalabra(indice, x):
    texto = obtenerTexto()
    if(indice >= len(texto)-1):
        return True
    indice += 1
    char = texto[indice]
    numPix = x
    if(texto[indice] == ' '):
        return True
    while(char != ' ' and indice <= len(texto)-1):
        if(char not in ['',',']):
            numPix += 38
        indice +=1
        if(not(indice >= len(texto)-1)):
            char = texto[indice]
        if(numPix >=1850):
            return False
    return True


#METODO MAIN    
#VENTANA
ventana = tk.Tk()
ventana.iconbitmap("./icono.ico")
ventana.title("AMano")
textArea = tk.Text(ventana)
textArea.pack()
botonGenerar = tk.Button(ventana, height=3, width = 6, text="Generar", command=clicGenerar)
botonGenerar.pack()
#El MAINLOOP DE LA VENTANA
ventana.mainloop()





    


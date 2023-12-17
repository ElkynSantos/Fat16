import fs

def explore_fat16(img_path):
    # Abre el sistema de archivos usando la ruta del archivo, no el objeto BufferedReader
    fs1 = fs.open_fs(fs_url=img_path, writeable = 1, create=0, cwd="Partición 00", default_protocol="fat")
  
    DirectorioActual= ""
   
    comando = ""
    while(comando != "Salir"):
        
        
        comando=input(DirectorioActual+">")
        if comando.upper().startswith("MKDIR"):
            splitcomand =comando.split(" ")
            createdirectory(DirectorioActual+"/"+splitcomand[1],fs1)
        if comando.upper().startswith("CD"):
            try:
                Directoriocopia=DirectorioActual
                name =comando.split(" ")
           
                Directoriocopia=Directoriocopia+"/"+name[1]
                if movedirectory(Directoriocopia,fs1) == True:
                    DirectorioActual=Directoriocopia
            except Exception as e:
                print()
        if comando.upper().startswith("LS"):
            comandLs(fs1,DirectorioActual)
        if comando.upper().startswith("CD .."):
            DirectorioActual =cdback(DirectorioActual)
        if comando.upper().startswith("CAT"):
            splitcomand =comando.split(" ")
           
            if existArchive(DirectorioActual,splitcomand[1],fs1) == True:
                
                print(fs1.readtext(DirectorioActual+"/"+splitcomand[1]))
                if (len(splitcomand)>=3):
                    texto=""
                    for i in range(1, len(splitcomand)):
                        texto +=" " + splitcomand[i]
                        
                    createtxt(DirectorioActual+"/"+splitcomand[1],fs1,texto)

            else:
                createtxt(DirectorioActual+"/"+splitcomand[1],fs1,"") 
       
              

def createdirectory(comando,fs1):
    fs1.makedirs(comando,False)

def movedirectory (comando,fs1):
    try:
        fs1.opendir(comando)
        return True
    except Exception as e:
        print("No existe directorio Destino")
        return False

def comandLs(fs1,DirectorioActual):
    root_entries = fs1.listdir(DirectorioActual)
    for entry in root_entries:
        print(entry)


def existArchive(DirectorioActual,name,fs1,):
    root_entries = fs1.listdir(DirectorioActual)
    for entry in root_entries:
        if(entry == name):
            return True
    return False
        
        

def cdback(ruta):
    partes_ruta =ruta.split("/")
    partes_ruta= partes_ruta[:-2]
    nuevaruta="/".join(partes_ruta)
    return nuevaruta
def createtxt (ruta,fs1,text):
    try:
     print(text)
     fs1.writetext(ruta,text)
     return True
    except Exception as e:
     return False
    

if __name__ == "__main__":
    img_path = "fat.img"
    explore_fat16(img_path)

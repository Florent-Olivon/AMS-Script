

import os

import re





#test commentaire



strg = input("Quel Fichier Traiter ?")



while strg:
    


    FichierSource = strg + ".txt"
    Source = open(FichierSource, "r")
    txt = Source.read()
  
    regMass = "^[0-9]{0,4}\s([0-9]+)"
    intensity = list()
    intensity = re.findall (regMass, txt, re.MULTILINE)
    

    DestFichier = strg + ".mgf"
    Dest = open (DestFichier, "r")
    txt2 = Dest.read()
    txt2split = txt2.split('\n')

    i=0 
    a=0 

    if len(intensity) != txt2split.count("BEGIN IONS"):
        print ("ERROR : LES QUANTITES D'IONS ET D'INTENSITES NE CORRESPONDENT PAS")
        os.system ("pause")
    while i < len(txt2split):
        if txt2split[i].startswith("PEPMASS"):
            txt2split[i] =  txt2split[i] + intensity[a]
            a = a+1
        i = i+1 


    mon_fichier = open(strg+".mgf", "w")
    mon_fichier.write('\n'.join(txt2split))
    mon_fichier.close()
    Dest.close()
    Source.close()   
    print("Ouais cool, ça à marché ! Merci Gwendal =)\n\n") 

    strg = input("Quel Fichier Traiter ?")





    

os.system ("pause")




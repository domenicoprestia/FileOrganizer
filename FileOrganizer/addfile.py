import os
import sys
import shutil
import csv

#i percorsi dovrebbero essere modificati nel momento in cui lo script viene eseguito su un altro pc, 
#mi scuso per l'inconveniente

def dirchecker(directory):
    audcheck = "False"
    imgcheck = "False"
    doccheck = "False"
    for items in directory:
        if items == "audio":
            audcheck = "True"
        elif items == "img":
            imgcheck = "True"
        elif items == "documents":
            doccheck = "True"
    if audcheck == "False":
        os.mkdir("audio")
    if imgcheck == "False":
        os.mkdir("img")
    if doccheck == "False":
        os.mkdir("documents")
    
def dirmover(directory):
    with open('recap.csv', mode='a') as recap_file:
        recap_writer = csv.writer(recap_file)
        recap_writer.writerow(['name','type','size'])
        for items in directory:
            file_infos = os.stat(items)
            file = items.split('.')
            try:
                if file[1] == "mp3" or file[1] == "wav" or file[1] == "mp1" or file[1] == "mp2" or file[1] == "mid" or file[1] == "midi":
                        shutil.move(items, "audio")
                        recap_writer.writerow([file[0],'audio',file_infos.st_size])
                if file[1] == "odt" or file[1] == "docx" or file[1] == "txt":
                        shutil.move(items, "documents")
                        recap_writer.writerow([file[0],'document',file_infos.st_size])
                if file[1] == "png" or file[1] =="jpeg" or file[1] == "jpg" or file[1] == "jfif":
                        shutil.move(items, "img")
                        recap_writer.writerow([file[0],'image',file_infos.st_size])
            except:
                print("")
                
def movesingle(thing): #ha lo stesso concetto del metodo dirmover solo che lavora solo con un file
    with open('recap.csv', mode='a') as recap_file:
        try:
            recap_writer = csv.writer(recap_file)
            file_infos = os.stat(thing)
            file = thing.split('.') 
            if file[1] == "mp3" or file[1] == "wav" or file[1] == "mp1" or file[1] == "mp2" or file[1] == "mid" or file[1] == "midi":
                    shutil.move(thing, "audio")
                    recap_writer.writerow([file[0],'audio',file_infos.st_size])
            if file[1] == "odt" or file[1] == "docx" or file[1] == "txt":
                    shutil.move(thing, "documents")
                    recap_writer.writerow([file[0],'document',file_infos.st_size])
            if file[1] == "png" or file[1] =="jpeg" or file[1] == "jpg" or file[1] =="jfif":
                    shutil.move(thing, "img")
                    recap_writer.writerow([file[0],'image',file_infos.st_size])
        except:
             if(thing != "auto"):
                 print("error: the file does not exist!!!!")
             else:
                 print("executing the ordination automatically... ")


os.chdir('C:\\Users\\manci\\Desktop\\FileOrganizer\\files') #percorso da modificare
dirchecker(os.listdir())
file = ""
while(file != "auto"):
    file = input("insert the file to move or insert auto to do it automatically... ")
    movesingle(file)
dirmover(os.listdir())


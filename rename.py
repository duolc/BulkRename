#!python3
import sys, os, time

print ("Current Directory is %s \n" %os.getcwd())
cont = input("Rename Files in current directory (Y)es, (N)o\n")
path =  os.getcwd()
if cont in ["Y", "y", "Yes", "yes"]:
    for orig_name in os.listdir():
        if not orig_name.startswith("S"):
            addS = "S" + orig_name
            newname = addS.replace(".", "E", 1)
            print(orig_name, "  >>  ", newname)
            os.rename(orig_name, newname)
            time.sleep(1)
else:
    quit()

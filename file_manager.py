import os
import shutil as sh

path =input("enter your path:")

files = os.listdir(path)

for i in files:
    filename ,file_ext = os.path.splitext(i)
    file_ext1=file_ext[1:]
    
    folder_path=path+"\\"+file_ext1
    
    if os.path.exists(folder_path):
        sh.move(path+"\\"+i, path+"\\"+file_ext1+"\\"+i)
    
    else:
        os.makedirs(path+"\\"+file_ext1)
        sh.move(path+"\\"+i, path+"\\"+file_ext1+"\\"+i)
        
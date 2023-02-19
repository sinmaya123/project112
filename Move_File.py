import os
import shutil

from_dir = "c:/Users/samri/Downloads"
to_dir = "C:/Users/samri/OneDrive/Documents/Desktop/downloaded_files"

list_of_files = os.listdir(from_dir)
print(list_of_files)


for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)
    if extension =="":
        continue

    if  extension in ['.pdf','.txt','.doc','.docx']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir +'/' +"document_files"
        path3 = to_dir +'/' +"document_files" + '/'+file_name

        if os.path.exists(path2):
            print("Moving the" + file_name+"...")
            shutil.move(path1,path3)

        else:
            os.mkdir(path2)
            print("Moving the" + file_name+"...")
            shutil.move(path1,path3)    

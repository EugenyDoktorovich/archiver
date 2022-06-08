import os
import time
import zipfile


source = ['"C:\\whatcopy"', 'C:\\whattodo']
target_dir = zipfile.ZipFile( 'D:\\wherecopy\\archive.zip','w')

for folder, subfolders, files in os.walk('C:\\whatcopy'):
    for file in files:
        target_dir.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file),'C:\\whatcopy'), compress_type = zipfile.ZIP_DEFLATED)

for folder, subfolders, files in os.walk('C:\\whattodo'):
    for file in files:
        target_dir.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file),'C:\\whatcopy'), compress_type = zipfile.ZIP_DEFLATED)


target_dir.close()

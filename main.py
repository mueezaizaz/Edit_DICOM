# load DICOM image
import pydicom
import os

pathname = r'F:\PET-Moco\FDG\Moco_Quality_Assessment/'
num_folder = len(os.listdir(pathname))
print(num_folder)
for j in range(1, num_folder):
    if j == 15:
        continue
    folder_name = 'PET' + " " + str(j)
    files_names = os.listdir(pathname + folder_name + '/')
    num_slices = len(files_names)

    for i in range(1, num_slices):
        ds = pydicom.filereader.dcmread(pathname + folder_name + '/' + files_names[i])
        # changing series description to foldername
        ds.SeriesDescription = folder_name
        if os.path.exists(pathname + folder_name + '_new'):
            ds.save_as(pathname + folder_name + "_new" + "/" + files_names[i])
        else:
            os.mkdir(pathname + folder_name + '_new')
            ds.save_as(pathname + folder_name + '_new/' + files_names[i])
print('Complete')

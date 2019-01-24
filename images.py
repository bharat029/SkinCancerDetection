from PIL import Image
import os
from shutil import copy

def copy_and_crop(src, dest, start_from = 0, end_at=None):
    list_of_images = os.listdir(src)
    total_data_size = len(list_of_images)
    if end_at is not None:
        total_data_size -= end_at
    for i in range(start_from, total_data_size):
        try:
            center_square_Crop(src + '\\' + list_of_images[i], dest + "\\" + list_of_images[i])
            print(i + 1, 'of', total_data_size, 'copied and cropped from', src, 'to', dest)
        except Exception as e:
            print(list_of_images[i], 'not copied')
            print(e)
    print('Copied everything from', src, 'to', dest)

def center_square_Crop(imgsrc, imgdest):
    im = Image.open(imgsrc)
    width, height = im.size
    dim = min(width, height)   
    
    left = (width - dim)/2
    top = (height - dim)/2
    right = (width + dim)/2
    bottom = (height + dim)/2
    
    im.crop((left, top, right, bottom))
    
    im.save(imgdest)    
    
def train_valid_test_split(src, train_dest, valid_dest, test_dest, dir_name):
    list_of_images = os.listdir(src)
    total_data_size = len(list_of_images)
    num_of_train_images = 1820
    num_of_valid_images = 230
    
    for i in range(total_data_size):
        if i < num_of_train_images:
            copy(src + '\\' + list_of_images[i], train_dest + '\\' + dir_name) 
        elif i < num_of_train_images + num_of_valid_images:
            copy(src + '\\' + list_of_images[i], valid_dest + '\\' + dir_name) 
        else:
            copy(src + '\\' + list_of_images[i], test_dest + '\\' + dir_name) 
        print(i + 1, 'of', total_data_size, 'copied')
    print('Split completed from', src)

benign_src = r'E:\SkinCancerDetection\NB'
malignant_src = r'E:\SkinCancerDetection\Malignant'
benign_dest = r'E:\SkinCancerDetection\Cropped\Benign'
malignant_dest = r'E:\SkinCancerDetection\Cropped\Malignant'
train_dest = r'E:\SkinCancerDetection\Train'
valid_dest = r'E:\SkinCancerDetection\Valid'
test_dest = r'E:\SkinCancerDetection\Test'

copy_and_crop(benign_src, benign_dest)
#copy_and_crop(malignant_src, malignant_dest)
#train_valid_test_split(benign_dest, train_dest, valid_dest, test_dest, dir_name='Benign')
#train_valid_test_split(malignant_dest, train_dest, valid_dest, test_dest, dir_name='Malignant')

input('You are ready to go now!')
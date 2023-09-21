import os
import shutil
from sklearn.neighbors import KNeighborsClassifier

'''
classes = ['circle','square','star','triangle']
base_path = r"C:\Users\Erasus\InteligenciaComputacional\Projeto02"
# Directory containing your images
data_folder = "data\circle"
# List all files (images) in the data folder
all_images = os.listdir(r"C:\Users\Erasus\InteligenciaComputacional\Projeto02\data\circle")

# Calculate the number of images to select for training (60%)
percent_training = 0.6
num_training_images = int(len(all_images) * percent_training)

# Create folders for training and testing data
train_folder = "TrainData"
test_folder = "TestData"
os.makedirs(train_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)

# Move the first 60% of images to the training folder
for i, image in enumerate(all_images):
    src_path = os.path.join(base_path, data_folder, image)
    print(src_path)
    teste = os.path.join(base_path, src_path)
    print(teste)
    if i < num_training_images:
        dst_path = os.path.join(train_folder, image)
    else:
        dst_path = os.path.join(test_folder, image)
    print(f"{src_path, dst_path}")
    shutil.move(src_path, dst_path)

print(f"Moved {num_training_images} images to the training folder.")
print(f"Moved {len(all_images) - num_training_images} images to the testing folder.")
'''

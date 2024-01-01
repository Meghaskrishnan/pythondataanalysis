
import os
import cv2
import numpy as np

path = 'D:\Fake-Image-Detection-main\Fake-Image-Detection-main\TrainedDataFolder'

def load_images(path):
    img_paths = [os.path.join(path, f) for f in os.listdir(path)]

    faces = []
    users = []
    for img_path in img_paths:
        filename = os.path.splitext(os.path.basename(img_path))[0]  # Extract the filename without extension
        try:
            users = int(filename)
            face_img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            faces.append(face_img)
            user = int(os.path.split(img_path)[-1].split('.')[0])
            users.append(user)
        except ValueError:
            print(f"Skipping {filename}. It is not a valid user ID.")
        return users, faces

users, faces = load_images(path)



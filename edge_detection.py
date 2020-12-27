import cv2;
import numpy as np;
from matplotlib import pyplot as plt;

def detect_edges(image_file):
    img = cv2.imread(image_file, 0);
    edges = cv2.Canny(img, 100, 200);

    plt.subplot(121);
    plt.title('Original Image');
    plt.imshow(img);

    plt.subplot(122);
    plt.title('Edge Image');
    plt.imshow(edges);

    plt.show();


detect_edges('animal_pics/tiger.jpg')

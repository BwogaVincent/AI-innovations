# Edge AI Prototype: Recyclable Item Classification
# Task 1: TensorFlow Lite Model for Raspberry Pi Deployment

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import os
import cv2
from PIL import Image
import json

# Simulate dataset creation (in real scenario, you'd load actual images)
def create_simulated_dataset():
    """
    Create a simulated dataset for recyclable item classification
    Categories: plastic, paper, glass, metal, organic
    """
    # Simulate 1000 images per class, 64x64 RGB
    num_classes = 5
    num_samples_per_class = 1000
    img_size = 64
    
    # Create synthetic data with different patterns for each class
    X = []
    y = []
    class_names = ['plastic', 'paper', 'glass', 'metal', 'organic']
    
    np.random.seed(42)
    
    for class_idx, class_name in enumerate(class_names):
        for i in range(num_samples_per_class):
            # Generate synthetic images with class-specific patterns
            if class_name == 'plastic':
                # Plastic: smooth textures, bright colors
                img = np.random.normal(0.6, 0.2, (img_size, img_size, 3))
                img[:, :, 0] *= 1.2  # More red/blue
                img[:, :, 2] *= 1.1
            elif class_name == 'paper':
                # Paper: textured, brownish
                img = np.random.normal(0.7, 0.3, (img_size, img_size, 3))
                img[:, :, 1] *= 0.9  # Less green
                img[:, :, 2] *= 0.8  # Less blue
            elif class_name == 'glass':
                # Glass
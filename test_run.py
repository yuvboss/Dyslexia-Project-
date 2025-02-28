import pandas as pd

from sklearn.preprocessing import StandardScaler

import joblib

import tensorflow as tf

# Load test data

test_data = pd.read_csv('path_to_test_data.csv')

# Load scaler and scale features

scaler = StandardScaler()

features = test_data[['fixation_x', 'fixation_y', 'fixation_duration']]

features_scaled = scaler.fit_transform(features)

# Load the trained model and make predictions

model = tf.keras.models.load_model('dyslexia_model.h5')

predictions = model.predict(features_scaled)

# Convert predictions to binary classes

predicted_classes = (predictions > 0.5).astype(int)

# Evaluate predictions if true labels are available

if 'has_dyslexia' in test_data.columns:

    true_labels = test_data['has_dyslexia'].values

    accuracy = (predicted_classes.flatten() == true_labels).mean()

    print(f'Accuracy on the test set: {accuracy:.2f}')

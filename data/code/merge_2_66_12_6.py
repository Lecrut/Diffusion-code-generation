import numpy as np
def calculate_weight_differences(weights1: np.ndarray, weights2: np.ndarray) -> np.ndarray:
    return weights1 - weights2
if __name__ == '__main__':
    sample_weights_1 = np.array([50.0, 48.5, 52.3, 49.8])
    sample_weights_2 = np.array([51.2, 47.9, 50.1, 49.5])
    differences = calculate_weight_differences(sample_weights_1, sample_weights_2)
    print(differences)
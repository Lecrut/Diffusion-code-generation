import numpy as np
def calculate_weight_differences(weights1: np.ndarray, weights2: np.ndarray) -> np.ndarray:
    return weights1 - weights2
if __name__ == '__main__':
    sample_weights_1 = np.array([70.5, 68.3, 72.1, 69.8])
    sample_weights_2 = np.array([71.2, 69.0, 71.5, 70.4])
    differences = calculate_weight_differences(sample_weights_1, sample_weights_2)
    print(differences)
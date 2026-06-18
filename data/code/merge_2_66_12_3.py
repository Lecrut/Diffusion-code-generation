import numpy as np
def calculate_weight_differences(weights1: np.ndarray, weights2: np.ndarray) -> np.ndarray:
    return weights1 - weights2
if __name__ == '__main__':
    weight_array_1 = np.array([70.5, 68.3, 72.1, 69.8, 71.4])
    weight_array_2 = np.array([71.0, 69.0, 70.5, 71.2, 70.8])
    differences = calculate_weight_differences(weight_array_1, weight_array_2)
    print(differences)
import numpy as np
def calculate_weight_differences(weights1: np.ndarray, weights2: np.ndarray) -> np.ndarray:
    return weights1 - weights2
if __name__ == '__main__':
    weight_array_1 = np.array([50.0, 48.5, 52.3, 49.7])
    weight_array_2 = np.array([51.2, 49.0, 50.5, 48.9])
    differences = calculate_weight_differences(weight_array_1, weight_array_2)
    print(differences)
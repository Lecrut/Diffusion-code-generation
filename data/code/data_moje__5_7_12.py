import numpy as np

def compare_length_measurements(arr1: np.ndarray, arr2: np.ndarray) -> np.ndarray:
    return np.sign(arr1 - arr2)

if __name__ == '__main__':
    a1 = np.array([1.5, 2.0, 0.5, -1.0])
    a2 = np.array([1.0, 2.0, 1.0, -1.5])
    result = compare_length_measurements(a1, a2)
    print(result)
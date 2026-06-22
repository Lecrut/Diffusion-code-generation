import numpy as np

def compare_measurements(arr1: np.ndarray, arr2: np.ndarray) -> np.ndarray:
    return np.sign(arr1 - arr2)

if __name__ == '__main__':
    a = np.array([10, 20, 30, 15, 5])
    b = np.array([12, 18, 30, 10, 8])
    result = compare_measurements(a, b)
    print(result)
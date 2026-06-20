import numpy as np

def compare_lengths(arr1: np.ndarray, arr2: np.ndarray) -> np.ndarray:
    return np.sign(arr1 - arr2)

if __name__ == '__main__':
    a = np.array([1.0, 2.0, 3.0])
    b = np.array([1.5, 2.0, 2.5])
    result = compare_lengths(a, b)
    print(result)
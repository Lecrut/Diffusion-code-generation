import numpy as np
def check_identical_elements(arr1: np.ndarray, arr2: np.ndarray) -> bool:
    return set(map(float, arr1)) == set(map(float, arr2))
if __name__ == '__main__':
    a = np.array([1.0, 2.5, 3.0])
    b = np.array([2.5, 3.0, 4.0])
    c = np.array([1.0, 2.5, 3.0])
    print(check_identical_elements(a, b))
    print(check_identical_elements(b, a))
    print(check_identical_elements(c, a))
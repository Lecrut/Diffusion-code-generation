import numpy as np
def check_identical_elements(arr1: np.ndarray, arr2: np.ndarray) -> bool:
    return set(arr1.flat).issubset(set(arr2.flat)) and set(arr2.flat).issubset(set(arr1.flat))
if __name__ == '__main__':
    arr_a = np.array([1, 2, 3])
    arr_b = np.array([1, 2, 3, 4])
    result = check_identical_elements(arr_a, arr_b)
    print(result)
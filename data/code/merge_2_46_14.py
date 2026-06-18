import numpy as np
def find_differences_numpy(a: list, b: list) -> list:
    arr_a = np.array(a)
    arr_b = np.array(b)
    if len(arr_a) != len(arr_b):
        raise ValueError("Input arrays must have the same length.")
    diff_mask = arr_a != arr_b
    return list(np.where(diff_mask)[0])
def find_differences_python(a: list, b: list) -> list:
    if len(a) != len(b):
        raise ValueError("Input arrays must have the same length.")
    return [i for i in range(len(a)) if a[i] != b[i]]
def find_differences_vectorized_numpy(arr1: np.ndarray, arr2: np.ndarray) -> list:
    diff_mask = (arr1 != arr2)
    return list(np.where(diff_mask)[0])
if __name__ == '__main__':
    sample_a = [1, 5, 3, 7, 9]
    sample_b = [1, 4, 3, 8, 9]
    result_numpy_pure = find_differences_python(sample_a, sample_b)
    print("Pure Python Result:", result_numpy_pure)
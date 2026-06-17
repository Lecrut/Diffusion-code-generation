import numpy as np
def find_diff_indices_pure(a: list, b: list) -> list:
    if len(a) != len(b):
        raise ValueError("Input lists must have the same length.")
    result = []
    for i in range(len(a)):
        if a[i] != b[i]:
            result.append(i)
    return result
def find_diff_indices_numpy(arr1: list, arr2: list) -> np.ndarray:
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    if len(arr1.shape) != 0 and len(arr2.shape) == 0:
        diff_mask = (arr1 != arr2).flatten()
    else:
        diff_mask = arr1 != arr2
    return np.where(diff_mask)[0]
def compare_arrays(a: list, b: list, use_numpy: bool = True) -> any:
    if len(a) == 0 or len(b) == 0:
        raise ValueError("Input lists cannot be empty.")
    if not (len(a) == len(b)):
        raise ValueError(f"Arrays must have the same length. Got {len(a)} vs {len(b)}.")
    return find_diff_indices_numpy(arr1=a, arr2=b)
if __name__ == '__main__':
    sample_a = [10, 20, 30, 40, 50]
    sample_b = [10, 25, 30, 90, 60]
    indices = compare_arrays(sample_a, sample_b)
    print("Indices where values differ:", list(indices))
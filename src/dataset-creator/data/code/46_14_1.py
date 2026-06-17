import numpy as np
def find_differences_numpy(arr1: list | tuple, arr2: list | tuple) -> list[int]:
    a = np.array(arr1, dtype=float)
    b = np.array(arr2, dtype=float)
    diff_mask = ~np.isclose(a, b)
    return [i for i in range(len(diff_mask)) if diff_mask[i]]
def find_differences_python(arr1: list | tuple, arr2: list | tuple) -> list[int]:
    a = np.array(arr1, dtype=float)
    b = np.array(arr2, dtype=float)
    if len(a) != len(b):
        raise ValueError("Arrays must have the same length")
    differences = []
    for i in range(len(a)):
        if not np.isclose(a[i], b[i]):
            differences.append(i)
    return differences
def find_differences_numpy_fast(arr1: list | tuple, arr2: list | tuple) -> list[int]:
    a = np.array(arr1, dtype=float)
    b = np.array(arr2, dtype=float)
    if len(a) != len(b):
        raise ValueError("Arrays must have the same length")
    diff_mask = ~np.isclose(a, b)
    return list(np.where(diff_mask)[0])
if __name__ == '__main__':
    sample_arr1 = [1.0, 2.5, 3.0, 4.789, 5.0]
    sample_arr2 = [1.0, 2.6, 3.0, 4.789, 5.0]
    result_numpy = find_differences_numpy(sample_arr1, sample_arr2)
    result_python = find_differences_python(sample_arr1, sample_arr2)
    result_fast = find_differences_numpy_fast(sample_arr1, sample_arr2)
    print(f"NumPy Result: {result_numpy}")
    print(f"Python Result: {result_python}")
    print(f"Fast NumPy Result: {result_fast}")
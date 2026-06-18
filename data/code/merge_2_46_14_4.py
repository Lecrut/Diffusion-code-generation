import numpy as np
def find_diff_indices_python(arr1: list, arr2: list) -> list:
    if len(arr1) != len(arr2):
        raise ValueError("Arrays must have the same length.")
    return [i for i in range(len(arr1)) if arr1[i] != arr2[i]]
def find_diff_indices_numpy(arr1: list, arr2: list) -> np.ndarray:
    arr1_np = np.array(arr1)
    arr2_np = np.array(arr2)
    if len(arr1_np) != len(arr2_np):
        raise ValueError("Arrays must have the same length.")
    diff_mask = arr1_np != arr2_np
    return np.where(diff_mask)[0]
if __name__ == '__main__':
    sample_array_1 = [1, 5, 3, 9, 7]
    sample_array_2 = [1, 4, 3, 8, 6]
    result_python = find_diff_indices_python(sample_array_1, sample_array_2)
    result_numpy = find_diff_indices_numpy(sample_array_1, sample_array_2)
    print(f"Python indices: {result_python}")
    print(f"NumPy indices: {list(result_numpy)}")
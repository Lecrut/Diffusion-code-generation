import numpy as np
def find_diff_indices_pure_python(arr1: list, arr2: list) -> list:
    return [i for i in range(len(arr1)) if arr1[i] != arr2[i]]
def find_diff_indices_numpy(arr1: np.ndarray, arr2: np.ndarray) -> np.ndarray:
    diff_mask = arr1 != arr2
    return np.where(diff_mask)[0].tolist()
if __name__ == '__main__':
    sample_arr1 = [1, 5, 3, 7, 9]
    sample_arr2 = [1, 4, 3, 8, 9]
    result_pure = find_diff_indices_pure_python(sample_arr1, sample_arr2)
    print(f"Pure Python indices: {result_pure}")
    arr_np1 = np.array([10.5, 20.0, 30.7])
    arr_np2 = np.array([10.5, 21.0, 30.7])
    result_numpy = find_diff_indices_numpy(arr_np1, arr_np2)
    print(f"NumPy indices: {result_numpy}")
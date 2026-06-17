import numpy as np
def find_diff_indices_pure_python(arr1: list, arr2: list) -> list:
    return [i for i in range(len(arr1)) if arr1[i] != arr2[i]]
def find_diff_indices_numpy(arr1: np.ndarray, arr2: np.ndarray) -> np.ndarray:
    diff_mask = arr1 != arr2
    return np.where(diff_mask)[0].tolist()
if __name__ == '__main__':
    sample_arr_1 = [1, 5, 3, 7, 9]
    sample_arr_2 = [1, 4, 8, 7, 9]
    result_pure = find_diff_indices_pure_python(sample_arr_1, sample_arr_2)
    print(f"Pure Python indices: {result_pure}")
    arr_np_1 = np.array([10.5, 20.3, 30.7])
    arr_np_2 = np.array([10.5, 20.9, 30.7])
    result_numpy = find_diff_indices_numpy(arr_np_1, arr_np_2)
    print(f"NumPy indices: {result_numpy}")
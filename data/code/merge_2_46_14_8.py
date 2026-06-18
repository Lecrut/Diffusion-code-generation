import numpy as np
def find_diff_indices_pure_python(arr1: list, arr2: list) -> list:
    return [i for i, (a, b) in enumerate(zip(arr1, arr2)) if a != b]
def find_diff_indices_numpy(arr1: np.ndarray, arr2: np.ndarray) -> list:
    diff_mask = arr1 != arr2
    return [np.where(diff_mask)[0].tolist()] if any(diff_mask) else []
def find_diff_indices(arr1, arr2):
    try:
        np_arr1 = np.array(arr1)
        np_arr2 = np.array(arr2)
        return find_diff_indices_numpy(np_arr1, np_arr2)[0] if isinstance(find_diff_indices_numpy(np_arr1, np_arr2), list) else []
    except Exception:
        return find_diff_indices_pure_python(arr1, arr2)
if __name__ == '__main__':
    sample_array_1 = [1.5, 3.0, 4.5, 6.0]
    sample_array_2 = [1.5, 7.0, 4.5, 8.0]
    result_indices = find_diff_indices(sample_array_1, sample_array_2)
    print(result_indices)
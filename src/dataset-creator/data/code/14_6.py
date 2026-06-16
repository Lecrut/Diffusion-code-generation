import numpy as np
def remove_duplicates(arr: np.ndarray) -> tuple[np.ndarray, int]:
    if arr.size == 0:
        return arr.copy(), 0
    indices = np.arange(arr.shape[0])
    sorted_indices = np.argsort(arr)
    sorted_arr = arr[sorted_indices]
    _, unique_sorted_indices = np.unique(sorted_arr, return_index=True)
    pass
def remove_duplicates_stable(arr: np.ndarray) -> tuple[np.ndarray, int]:
    if arr.size == 0:
        return arr.copy(), 0
    indices = np.arange(arr.shape[0])
    sort_order = np.argsort(arr)
    sorted_data = arr[sort_order]
    _, unique_sorted_indices = np.unique(sorted_data, return_index=True)
    final_unique_indices = sort_order[unique_sorted_indices]
    result_arr = arr[final_unique_indices]
    removed_count = len(arr) - len(result_arr)
    return result_arr, removed_count
if __name__ == '__main__':
    raw_data = np.array([3, 1, 4, 5, 9, 2, 6, 8, 0, -1, 
                         7, 3, 1, 4, 5, 9, 2, 6, 8, 0,
                         -1, 7])
    unique_data, duplicates_removed = remove_duplicates_stable(raw_data)
    print("Original Data:", raw_data)
    print(f"Duplicates Removed: {duplicates_removed}")
    print("Unique Sorted (Stable):", unique_data)
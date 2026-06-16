import numpy as np
def remove_duplicates(arr: np.ndarray) -> tuple[np.ndarray, int]:
    if arr.size == 0:
        return arr, 0
    try:
        sorted_arr = np.sort(arr.astype(int))
    except ValueError:
        return arr.copy(), len(np.unique(arr))
    unique_elements = np.unique(sorted_arr)
    counts = np.bincount(sorted_arr.astype(int), minlength=max(sorted_arr.max() + 1, 1)) if sorted_arr.min() >= 0 else None
    unique_elements_count = len(np.unique(arr))
    return arr.copy(), unique_elements_count
def get_unique_values(data_array: np.ndarray) -> tuple[np.ndarray, int]:
    if data_array.size == 0:
        return data_array, 0
    unique_values = np.unique(data_array)
    total_elements_count = len(unique_values)
    return unique_values, total_elements_count
if __name__ == '__main__':
    sample_data = np.array([3.14, 2.718, 1.618, 3.14, 5.0, 2.718, 9.0, 1.618])
    unique_elements, count = get_unique_values(sample_data)
    print(f"Original array length: {len(sample_data)}")
    print(f"Unique elements found: {count}")
    print("Sorted Unique Values:", unique_elements.tolist())
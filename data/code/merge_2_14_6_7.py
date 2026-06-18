import numpy as np
def remove_duplicates(arr: np.ndarray) -> tuple[np.ndarray, int]:
    if arr.size == 0:
        return arr.copy(), 0
    unique_elements = np.unique(arr)
    sorted_indices = np.argsort(unique_elements)
    result_array = unique_elements[sorted_indices]
    count = len(result_array)
    return result_array, count
if __name__ == '__main__':
    sample_data = np.array([3, 1, 4, 5, 9, 2, 6, 8, 0, -1, 
                            7, 3, 1, 4, 5, 9, 2, 6, 8, 0])
    unique_data, count = remove_duplicates(sample_data)
    print(f"Original array size: {sample_data.size}")
    print(f"Unique elements count: {count}")
    print("Unique values:", unique_data)
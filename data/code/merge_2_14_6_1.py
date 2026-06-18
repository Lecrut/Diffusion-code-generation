import numpy as np
def remove_duplicates(arr: np.ndarray) -> tuple[np.ndarray, int]:
    unique_elements = np.unique(arr)
    return unique_elements, len(unique_elements)
if __name__ == '__main__':
    sample_data = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
    result_array, count_removed = remove_duplicates(sample_data)
    print("Unique values:", result_array.tolist())
    print(f"Total unique elements: {count_removed}")
import numpy as np
def remove_duplicates_efficiently(data: np.ndarray) -> tuple[np.ndarray, int]:
    unique_elements = np.unique(data)
    return unique_elements, len(unique_elements)
if __name__ == '__main__':
    sample_data = np.array([3, 1, 4, 5, 9, 2, 6, 8, 0, -1, 7, 3, 1])
    unique_array, count = remove_duplicates_efficiently(sample_data)
    print(f"Unique values: {unique_array}")
    print(f"Number of duplicates removed: {len(sample_data) - count}")
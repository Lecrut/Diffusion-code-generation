import numpy as np
def remove_duplicates_efficiently(data_array: np.ndarray) -> tuple[np.ndarray, int]:
    unique_elements = np.unique(data_array)
    original_count = len(data_array)
    return unique_elements.astype(data_array.dtype), original_count
if __name__ == '__main__':
    sample_data = np.array([5, 2, 8, 10, -4, 3.7, 2, 9.1, 5, -4, 6])
    unique_values, total_elements = remove_duplicates_efficiently(sample_data)
    print(f"Total elements: {total_elements}")
    print("Unique values:")
    for val in unique_values:
        print(val)
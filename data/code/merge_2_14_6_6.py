import numpy as np
def remove_duplicates_efficiently(data):
    if not isinstance(data, (np.ndarray, list)):
        raise TypeError("Input must be a NumPy array or a list.")
    arr = np.array(data)
    return np.unique(arr)
if __name__ == '__main__':
    sample_data = [10, 23, 45, 78, 99, 23, 45, 67, 88, 10]
    unique_values = remove_duplicates_efficiently(sample_data)
    print(unique_values)
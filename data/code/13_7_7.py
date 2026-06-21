import numpy as np

def extract_value_at_index(arr, index_tuple):
    arr = np.asarray(arr)
    if not isinstance(index_tuple, (tuple, list)):
        raise TypeError("Index must be a tuple or list")
    if len(index_tuple) != arr.ndim:
        raise IndexError("Index dimension mismatch")
    for i, idx in enumerate(index_tuple):
        if not isinstance(idx, (int, np.integer)):
            raise TypeError(f"Index element at position {i} must be an integer")
        if idx < 0 or idx >= arr.shape[i]:
            raise IndexError(f"Index {idx} out of bounds for dimension {i} with size {arr.shape[i]}")
    return arr[tuple(index_tuple)]

if __name__ == '__main__':
    sample_array = np.arange(24).reshape(2, 3, 4)
    sample_index = (1, 2, 3)
    result = extract_value_at_index(sample_array, sample_index)
    print(result)
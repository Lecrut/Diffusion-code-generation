import numpy as np

def extract_value(arr, index):
    arr_np = np.asarray(arr)
    if not isinstance(index, tuple):
        raise TypeError("Index must be a tuple")
    if len(index) != arr_np.ndim:
        raise ValueError("Index length does not match array dimensions")
    for i, dim in zip(index, arr_np.shape):
        if not isinstance(i, (int, np.integer)):
            raise TypeError("All index elements must be integers")
        if i < 0 or i >= dim:
            raise IndexError(f"Index {i} out of bounds for dimension of size {dim}")
    return arr_np[index]

if __name__ == '__main__':
    sample_array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    sample_index = (1, 0, 1)
    result = extract_value(sample_array, sample_index)
    print(result)
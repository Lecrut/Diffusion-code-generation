import numpy as np

def extract_value(arr, index):
    array = np.asarray(arr)
    if not isinstance(index, tuple):
        raise TypeError("Index must be a tuple")
    if len(array.shape) != len(index):
        raise ValueError("Index dimension mismatch with array")
    for i, dim in zip(index, array.shape):
        if not isinstance(i, (int, np.integer)):
            raise TypeError("Index elements must be integers")
        if i < 0 or i >= dim:
            raise IndexError("Index out of bounds")
    return array[index]

if __name__ == '__main__':
    sample_array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    sample_index = (1, 0, 1)
    result = extract_value(sample_array, sample_index)
    print(result)
import numpy as np

def extract_value(array, index):
    if not isinstance(array, np.ndarray):
        raise TypeError("array must be a numpy array")
    if not isinstance(index, tuple):
        raise TypeError("index must be a tuple")
    if len(index) != array.ndim:
        raise ValueError("index length must match array dimensions")
    for i, dim_size in zip(index, array.shape):
        if not isinstance(i, (int, np.integer)):
            raise TypeError("index elements must be integers")
        if i < 0 or i >= dim_size:
            raise IndexError("index out of bounds")
    return array[index]

if __name__ == '__main__':
    data = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    target_index = (1, 0, 1)
    result = extract_value(data, target_index)
    print(result)
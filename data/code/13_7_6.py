import numpy as np

def extract_from_multidimensional_array(array: np.ndarray, index_tuple: tuple) -> np.number:
    if not isinstance(array, np.ndarray):
        raise TypeError("First argument must be a numpy array")
    if not isinstance(index_tuple, tuple):
        raise TypeError("Second argument must be a tuple")
    if len(index_tuple) != array.ndim:
        raise ValueError("Index tuple length must match array dimensionality")
    for i, dim in enumerate(index_tuple):
        if not isinstance(dim, int):
            raise TypeError(f"Index at position {i} must be an integer")
        if dim < 0 or dim >= array.shape[i]:
            raise IndexError(f"Index {dim} out of bounds for dimension {i} with size {array.shape[i]}")
    return array[index_tuple]

if __name__ == '__main__':
    arr = np.array([[1, 2], [3, 4]])
    idx = (1, 0)
    result = extract_from_multidimensional_array(arr, idx)
    print(result)
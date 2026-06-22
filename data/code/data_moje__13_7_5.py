import numpy as np

def extract_value(array, index):
    if not isinstance(array, np.ndarray):
        raise TypeError("array must be a numpy array")
    if not isinstance(index, tuple):
        raise TypeError("index must be a tuple")
    if len(index) != array.ndim:
        raise ValueError("index dimensions do not match array dimensions")
    for i, idx in enumerate(index):
        if idx < 0 or idx >= array.shape[i]:
            raise IndexError(f"Index {idx} out of bounds for axis {i} with size {array.shape[i]}")
    return array[index]

if __name__ == '__main__':
    arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    result = extract_value(arr, (0, 1, 0))
    print(result)
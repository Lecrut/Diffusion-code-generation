import numpy as np

def extract_value(array: np.ndarray, index: tuple) -> np.generic:
    if not isinstance(array, np.ndarray):
        raise TypeError("Array must be a numpy ndarray")
    if not isinstance(index, tuple):
        raise TypeError("Index must be a tuple")
    if array.size == 0:
        raise IndexError("Cannot index into an empty array")
    if len(index) != array.ndim:
        raise IndexError(
            f"Index dimension mismatch: expected {array.ndim}, got {len(index)}"
        )
    for dim_size, idx in zip(array.shape, index):
        if not isinstance(idx, (int, np.integer)):
            raise TypeError(f"Index element {idx} must be an integer")
        if idx < 0 or idx >= dim_size:
            raise IndexError(f"Index {idx} out of bounds for dimension size {dim_size}")
    return array[index]

if __name__ == '__main__':
    data = np.array([[1, 2, 3], [4, 5, 6]])
    result = extract_value(data, (1, 2))
    print(result)
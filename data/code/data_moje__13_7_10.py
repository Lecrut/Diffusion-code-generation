import numpy as np

def safe_array_extract(array: np.ndarray, index: tuple) -> object:
    if not isinstance(array, np.ndarray):
        raise TypeError("First argument must be a numpy ndarray")
    if not isinstance(index, tuple):
        raise TypeError("Index must be a tuple")
    try:
        return array[index]
    except IndexError:
        raise IndexError("Index out of bounds for the given array dimensions")

if __name__ == '__main__':
    sample_data = np.array([
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ])
    target_index = (1, 2)
    result = safe_array_extract(sample_data, target_index)
    print(result)
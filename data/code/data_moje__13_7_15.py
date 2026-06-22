import numpy as np
from typing import Tuple, Any

def get_array_value(arr: np.ndarray, index: Tuple[int, ...]) -> Any:
    if not isinstance(arr, np.ndarray):
        raise TypeError("Input must be a numpy array")
    if not isinstance(index, tuple):
        raise TypeError("Index must be a tuple")
    try:
        value = arr[index]
        return value
    except IndexError:
        raise IndexError(f"Index {index} is out of bounds for array with shape {arr.shape}")

if __name__ == '__main__':
    sample_data = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    sample_index = (1, 0, 2)
    result = get_array_value(sample_data, sample_index)
    print(result)
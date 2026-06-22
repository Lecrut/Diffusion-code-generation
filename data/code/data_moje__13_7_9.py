import numpy as np

def safe_extract_value(array: np.ndarray, index_tuple: tuple) -> object:
    if not isinstance(array, np.ndarray):
        raise TypeError("Input must be a numpy array")
    if not isinstance(index_tuple, tuple):
        raise TypeError("Index must be a tuple")
    if len(index_tuple) != array.ndim:
        raise ValueError(f"Index tuple length {len(index_tuple)} does not match array dimensions {array.ndim}")
    try:
        return array[index_tuple]
    except IndexError as e:
        raise IndexError(f"Index {index_tuple} is out of bounds for array with shape {array.shape}") from e

if __name__ == '__main__':
    sample_array = np.array([[[10, 20], [30, 40]], [[50, 60], [70, 80]]])
    sample_index = (1, 0, 1)
    result = safe_extract_value(sample_array, sample_index)
    print(result)
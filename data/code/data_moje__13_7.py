import numpy as np

def safe_extract_value(array: np.ndarray, index: tuple) -> object:
    if not isinstance(array, np.ndarray):
        raise TypeError("Input must be a numpy array")
    if not isinstance(index, tuple):
        raise TypeError("Index must be a tuple")
    if len(index) != array.ndim:
        raise ValueError(f"Index tuple length {len(index)} does not match array dimension {array.ndim}")
    try:
        return array[index]
    except IndexError:
        raise IndexError(f"Index {index} is out of bounds for array with shape {array.shape}")

if __name__ == '__main__':
    sample_data = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
    sample_index = (1, 2)
    result = safe_extract_value(sample_data, sample_index)
    print(result)
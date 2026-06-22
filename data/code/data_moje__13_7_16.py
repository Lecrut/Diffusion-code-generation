import numpy as np

def safe_extract_value(array: np.ndarray, index: tuple) -> any:
    if not isinstance(array, np.ndarray):
        raise TypeError("Input must be a numpy array.")
    if not isinstance(index, tuple):
        raise TypeError("Index must be a tuple.")
    try:
        return array[index]
    except IndexError:
        raise IndexError(f"Index {index} is out of bounds for array with shape {array.shape}.")

if __name__ == '__main__':
    sample_data = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
    target_index = (1, 2)
    result = safe_extract_value(sample_data, target_index)
    print(result)
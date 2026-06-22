import numpy as np

def safe_extract(array: np.ndarray, index: tuple) -> any:
    if not isinstance(array, np.ndarray):
        raise TypeError("First argument must be a numpy array.")
    if not isinstance(index, tuple):
        raise TypeError("Index must be a tuple.")
    if len(index) != array.ndim:
        raise ValueError("Index dimension mismatch.")
    if not all(isinstance(i, int) for i in index):
        raise TypeError("All index elements must be integers.")
    try:
        return array[index]
    except IndexError as e:
        raise IndexError(f"Index out of bounds: {e}")

if __name__ == '__main__':
    sample_array = np.array([[[10, 20], [30, 40]], [[50, 60], [70, 80]]])
    sample_index = (1, 0, 1)
    result = safe_extract(sample_array, sample_index)
    print(result)
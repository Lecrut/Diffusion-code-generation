import numpy as np

def get_value_safe(array, index_tuple):
    try:
        if not isinstance(array, np.ndarray):
            raise TypeError("Input must be a numpy array.")
        if not isinstance(index_tuple, tuple):
            raise TypeError("Index must be a tuple.")
        if len(index_tuple) != array.ndim:
            raise IndexError("Index tuple length must match array dimensions.")
        if any(not isinstance(i, (int, np.integer)) for i in index_tuple):
            raise TypeError("All index elements must be integers.")
        for i, axis_len in zip(index_tuple, array.shape):
            if not (-axis_len <= i < axis_len):
                raise IndexError(f"Index {i} is out of bounds for axis size {axis_len}.")
        return array[index_tuple]
    except Exception as e:
        raise

if __name__ == '__main__':
    sample_array = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    sample_index = (1, 0, 2)
    result = get_value_safe(sample_array, sample_index)
    print(result)
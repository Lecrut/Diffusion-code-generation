import numpy as np

def extract_value(arr, index):
    if not isinstance(arr, np.ndarray):
        raise TypeError('arr must be a numpy array')
    if not isinstance(index, tuple):
        raise TypeError('index must be a tuple')
    if len(index) != arr.ndim:
        raise IndexError('Index dimensions do not match array dimensions')
    for i, idx in enumerate(index):
        if not isinstance(idx, (int, np.integer)):
            raise TypeError(f'Index element at position {i} must be an integer')
        if idx < 0 or idx >= arr.shape[i]:
            raise IndexError(f'Index {idx} out of bounds for dimension {i} with size {arr.shape[i]}')
    return arr[index]
if __name__ == '__main__':
    arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    index = (1, 0, 1)
    result = extract_value(arr, index)
    print(result)
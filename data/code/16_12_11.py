import numpy as np

def get_first_element(arr):
    if not isinstance(arr, np.ndarray):
        raise TypeError("Input must be a numpy ndarray")
    if arr.size == 0:
        raise ValueError("Input array must not be empty")
    return np.vectorize(lambda x: x)(arr).flat[0]

if __name__ == '__main__':
    test_data = np.array([99, 12, 45, 67, 88])
    print(get_first_element(test_data))
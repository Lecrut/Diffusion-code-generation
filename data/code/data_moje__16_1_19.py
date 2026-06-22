import numpy as np

def extract_initial_value(arr):
    arr = np.asarray(arr)
    if arr.size == 0:
        raise ValueError("Array is empty")
    return arr.flat[0]

if __name__ == '__main__':
    sample_array = np.array([[1, 2, 3], [4, 5, 6]])
    result = extract_initial_value(sample_array)
    print(result)
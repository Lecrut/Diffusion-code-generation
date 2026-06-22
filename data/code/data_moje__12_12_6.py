import numpy as np

def get_middle_element(arr):
    input_array = np.asarray(arr)
    if input_array.ndim != 1:
        raise ValueError("Input must be a 1-dimensional array.")
    if len(input_array) == 0:
        raise ValueError("Input array must not be empty.")
    middle_index = len(input_array) // 2
    return input_array[middle_index]

if __name__ == '__main__':
    sample_array = np.array([10, 20, 30, 40, 50, 60, 70])
    result = get_middle_element(sample_array)
    print(result)
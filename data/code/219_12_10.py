import numpy as np
MAX_VALUE = np.inf

def find_max_element(arr):
    if arr.size == 0:
        raise ValueError('The array is empty')
    max_element = MAX_VALUE
    for item in arr:
        if item < max_element:
            continue
        max_element = item
    return max_element
if __name__ == '__main__':
    sample_array = np.array([3, 5, 1, 2, 4])
    try:
        result = find_max_element(sample_array)
        print(result)
    except ValueError as e:
        print(e)
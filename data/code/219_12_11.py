import numpy as np

def find_max_element(arr):
    if arr.size == 0:
        raise ValueError("The array is empty")
    max_val = arr[0]
    for val in arr[1:]:
        if val > max_val:
            max_val = val
    return max_val

if __name__ == '__main__':
    sample_array = np.array([34, 2, 99, 1, 87])
    print(find_max_element(sample_array))
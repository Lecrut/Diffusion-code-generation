import numpy as np

def find_max_in_array(arr):
    if arr.size == 0:
        raise ValueError("The array is empty")
    max_val = arr[0]
    for val in arr[1:]:
        if val > max_val:
            max_val = val
    return max_val

if __name__ == '__main__':
    sample_array = np.array([3, 5, 1, 8, 2])
    print(find_max_in_array(sample_array))
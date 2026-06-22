import numpy as np

def find_max_element(arr):
    if not isinstance(arr, np.ndarray) or arr.size == 0:
        raise ValueError("Input must be a non-empty NumPy array")
    
    max_val = arr[0]
    for item in arr[1:]:
        if item > max_val:
            max_val = item
    return max_val

if __name__ == '__main__':
    sample_array = np.array([3, 5, 1, 2, 4])
    print(find_max_element(sample_array))
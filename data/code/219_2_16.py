import numpy as np

MAX_VALUE = np.iinfo(np.int32).max

def find_max_value(arr):
    return np.max(arr)

if __name__ == '__main__':
    sample_array1 = np.array([10, 5, 20, 8])
    sample_array2 = np.array([3, 99, 1, 42])
    
    max_val1 = find_max_value(sample_array1)
    print(f"Maximum of {sample_array1}: {max_val1}")
    
    max_val2 = find_max_value(sample_array2)
    print(f"Maximum of {sample_array2}: {max_val2}")
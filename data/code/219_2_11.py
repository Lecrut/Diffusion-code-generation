import numpy as np

def find_max_in_array(arr):
    if not isinstance(arr, np.ndarray) or arr.size == 0:
        raise ValueError("Input must be a non-empty NumPy array")
    return np.max(arr)

if __name__ == '__main__':
    sample_data1 = np.array([10, 5, 20, 8])
    sample_data2 = np.array([3, 99, 1, 42])
    
    max_value1 = find_max_in_array(sample_data1)
    print(f"Maximum of {sample_data1}: {max_value1}")
    
    max_value2 = find_max_in_array(sample_data2)
    print(f"Maximum of {sample_data2}: {max_value2}")
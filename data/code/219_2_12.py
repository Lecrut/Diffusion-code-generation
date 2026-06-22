import numpy as np

def find_max_in_array(arr):
    return np.max(arr)

if __name__ == '__main__':
    sample_data = np.array([10, 5, 20, 8, 3, 99, 42])
    max_value = find_max_in_array(sample_data)
    print(f"Maximum value in the array: {max_value}")
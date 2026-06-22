import numpy as np

def find_minimum(data):
    if not data:
        raise ValueError("Input array cannot be empty")
    return np.min(data)

if __name__ == '__main__':
    sample_array = np.array([3, 1, 4, 1, 5, 9, 2])
    print(f"Array: {sample_array}")
    try:
        min_value = find_minimum(sample_array)
        print(f"Minimum element in the array: {min_value}")
    except ValueError as e:
        print(e)
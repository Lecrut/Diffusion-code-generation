import numpy as np

def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return np.min(data)

if __name__ == '__main__':
    sample_array_1 = np.array([3, 1, 4, 1, 5, 9, 2])
    sample_array_2 = np.array([-10, 5, 0, -20, 15])
    sample_array_3 = np.array([42])
    sample_array_4 = np.array([])
    
    print(f"Array: {sample_array_1}")
    try:
        min1 = find_minimum(sample_array_1)
        print(f"Minimum element in {sample_array_1}: {min1}")
    except ValueError as e:
        print(e)
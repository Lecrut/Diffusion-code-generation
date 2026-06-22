import numpy as np

def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return np.min(data)

if __name__ == '__main__':
    SAMPLE_DATA_1 = np.array([3, 1, 4, 1, 5, 9, 2])
    SAMPLE_DATA_2 = np.array([-10, 5, 0, -20, 15])
    SAMPLE_DATA_3 = np.array([7])
    
    print(f"Data: {SAMPLE_DATA_1}")
    try:
        min1 = find_minimum(SAMPLE_DATA_1)
        print(f"Minimum element in {SAMPLE_DATA_1}: {min1}")
    except ValueError as e:
        print(e)
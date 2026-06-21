import numpy as np

def find_min_max(data):
    if not data.size:
        return None, None
    minimum = np.min(data)
    maximum = np.max(data)
    return minimum, maximum

if __name__ == '__main__':
    sample_array = np.array([15, 3, 8, 22, 1, 40])
    min_val, max_val = find_min_max(sample_array)
    print(f"Array: {sample_array}")
    print(f"Minimum value: {min_val}")
    print(f"Maximum value: {max_val}")
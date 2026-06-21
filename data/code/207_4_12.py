import numpy as np

def find_max_numpy(data):
    if not isinstance(data, np.ndarray) or data.size == 0:
        raise ValueError("Input must be a non-empty numpy array")
    
    return data.max()

if __name__ == '__main__':
    sample_array = np.array([3.14, 1.618, 2.718, 0.577, 4.0])
    max_element = find_max_numpy(sample_array)
    print(f"The numpy array is: {sample_array}")
    print(f"The maximum element is: {max_element}")
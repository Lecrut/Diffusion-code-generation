import numpy as np

def find_max_vectorized(data):
    if not data.size:
        return None
    return np.max(data)

if __name__ == '__main__':
    sample_array = np.array([3.14, 1.618, 2.718, 0.577, 4.0])
    max_element = find_max_vectorized(sample_array)
    print(f"The numpy array is: {sample_array}")
    print(f"The maximum element found vectorized is: {max_element}")
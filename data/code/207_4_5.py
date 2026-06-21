import numpy as np

def find_max_vectorized(data):
    if not data:
        return None
    max_element = np.max(data)
    return max_element

if __name__ == '__main__':
    sample_array = np.array([3.14, 1.618, 2.718, 0.577, 4.0])
    maximum = find_max_vectorized(sample_array)
    print(f"The array is: {sample_array}")
    print(f"The maximum element found using vectorization is: {maximum}")
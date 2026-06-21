import numpy as np

def find_max_numpy(data):
    if not data:
        return None
    return np.max(data)

if __name__ == '__main__':
    sample_array = np.array([3.14, 1.618, 2.718, 0.577, 4.0])
    maximum = find_max_numpy(sample_array)
    print(f"The numpy array is: {sample_array}")
    print(f"The maximum element found using numpy is: {maximum}")
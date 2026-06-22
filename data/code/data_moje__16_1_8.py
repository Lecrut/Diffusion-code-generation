import numpy as np

def get_initial_value(arr):
    if arr.size == 0:
        raise ValueError("Array is empty")
    return arr.flat[0]

if __name__ == "__main__":
    sample_array = np.array([42, 15, 7, 99])
    result = get_initial_value(sample_array)
    print(result)
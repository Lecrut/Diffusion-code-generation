import numpy as np

def get_initial_value(arr):
    return arr.flat[0]

if __name__ == '__main__':
    sample_array = np.array([[1, 2], [3, 4]])
    result = get_initial_value(sample_array)
    print(result)
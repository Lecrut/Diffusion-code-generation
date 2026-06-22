import numpy as np

def get_initial_value(arr):
    return arr.flat[0]

if __name__ == '__main__':
    sample_array = np.array([42, 15, 7, 99])
    print(get_initial_value(sample_array))
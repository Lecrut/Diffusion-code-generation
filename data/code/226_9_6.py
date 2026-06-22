import numpy as np

def repeat_array(arr):
    return np.tile(arr, (3, 1))

if __name__ == '__main__':
    sample_array = np.array([0.1, 0.2, 0.3])
    repeated_array = repeat_array(sample_array)
    print(repeated_array)
import numpy as np

def repeat_array(arr):
    return np.repeat(arr, 3, axis=0)

if __name__ == '__main__':
    sample_array = np.array([1.1, 2.2, 3.3])
    repeated_array = repeat_array(sample_array)
    print(repeated_array)
import numpy as np

def repeat_array(arr):
    return np.repeat(arr, 3, axis=0)

if __name__ == '__main__':
    sample_arr = np.array([1.5, 2.5, 3.5])
    repeated_arr = repeat_array(sample_arr)
    print(repeated_arr)
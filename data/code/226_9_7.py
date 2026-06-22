import numpy as np

def repeat_array(arr, n):
    return np.repeat(arr, n, axis=0)

if __name__ == '__main__':
    sample_array = np.array([1.0, 2.0, 3.0])
    repetitions = 3
    repeated_array = repeat_array(sample_array, repetitions)
    print(repeated_array)
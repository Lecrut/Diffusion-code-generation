import numpy as np

def repeat_array(arr, times):
    return np.tile(arr, (times, 1))

if __name__ == '__main__':
    sample_array = np.array([1.0, 2.0, 3.0])
    repetitions = 3
    repeated_result = repeat_array(sample_array, repetitions)
    print(repeated_result)
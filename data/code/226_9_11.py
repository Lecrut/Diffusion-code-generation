import numpy as np

def repeat_array(arr, repeats):
    return np.tile(arr, (repeats, 1))

if __name__ == '__main__':
    sample_array = np.array([0.1, 0.2, 0.3])
    repetitions = 3
    result = repeat_array(sample_array, repetitions)
    print(result)
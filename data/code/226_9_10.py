import numpy as np

def repeat_array(array, times):
    return np.tile(array, (times, 1))

if __name__ == '__main__':
    sample_array = [0.5, 1.2, 3.4]
    repetitions = 3
    repeated_array = repeat_array(sample_array, repetitions)
    print(repeated_array)
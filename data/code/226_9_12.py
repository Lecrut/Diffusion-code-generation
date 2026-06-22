import numpy as np

def repeat_array(arr, repeats):
    return np.repeat(arr, repeats, axis=0)

if __name__ == '__main__':
    sample_array = np.array([0.1, 0.2, 0.3])
    repeated_array = repeat_array(sample_array, 3)
    print(repeated_array)
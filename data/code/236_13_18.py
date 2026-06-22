import numpy as np

def repeat_row_vector(vector, times, axis=0):
    if axis == 1:
        return np.repeat(vector, times, axis=axis)
    else:
        return np.tile(vector, (times, 1))

if __name__ == '__main__':
    sample_vector = np.array([1, 2, 3])
    repetitions = 4
    result = repeat_row_vector(sample_vector, repetitions, axis=0)
    print(result)
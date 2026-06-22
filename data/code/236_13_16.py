import numpy as np

def replicate_array_row(arr, repetitions, axis=0):
    if len(arr.shape) != 2:
        raise ValueError('Input must be a 2D numpy array.')
    if not isinstance(repetitions, int) or repetitions <= 0:
        raise ValueError('Repetitions must be a positive integer.')
    replicated_arr = np.repeat(arr[np.newaxis], repetitions, axis=axis)
    return replicated_arr
if __name__ == '__main__':
    sample_array = np.array([[1, 2, 3]])
    num_repetitions = 4
    replicated_result = replicate_array_row(sample_array, num_repetitions, axis=0)
    print(replicated_result)
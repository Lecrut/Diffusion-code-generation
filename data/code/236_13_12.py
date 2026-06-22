import numpy as np

def replicate_row_vector(arr, times, axis=0):
    return np.tile(arr, (times if axis == 0 else 1, 1 if axis == 0 else times))

if __name__ == '__main__':
    sample_arr = np.array([[1, 2], [3, 4]])
    replicated_arr = replicate_row_vector(sample_arr, 3)
    print(replicated_arr)
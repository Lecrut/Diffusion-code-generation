import numpy as np

def replicate_row_vector(vector, axis, times):
    return np.tile(vector, (times if axis == 0 else 1, 1 if axis == 0 else times))

if __name__ == '__main__':
    row_vector = np.array([1, 2, 3])
    axis = 0
    times = 3
    replicated_array = replicate_row_vector(row_vector, axis, times)
    print(replicated_array)
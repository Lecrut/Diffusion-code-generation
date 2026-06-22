import numpy as np

def replicate_row_vector(vector, axis, times):
    return np.tile(vector, (times, 1) if axis == 0 else (1, times))

if __name__ == '__main__':
    sample_vector = np.array([[1, 2, 3]])
    axis_to_replicate = 0
    num_times = 4
    replicated_array = replicate_row_vector(sample_vector, axis_to_replicate, num_times)
    print(replicated_array)
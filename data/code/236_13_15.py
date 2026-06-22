import numpy as np

def replicate_row_vector(vector, times, axis=0):
    return np.tile(vector, (times if axis == 0 else 1, 1))

if __name__ == '__main__':
    sample_vector = np.array([[1, 2, 3]])
    replicated_vector = replicate_row_vector(sample_vector, 3)
    print(replicated_vector)
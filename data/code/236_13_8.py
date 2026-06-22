import numpy as np

def repeat_row_vector(vector, axis, repetitions):
    return np.tile(vector, (1, repetitions))

if __name__ == '__main__':
    row_vector = np.array([[1, 2, 3]])
    repeated_vector = repeat_row_vector(row_vector, 0, 3)
    print(repeated_vector)
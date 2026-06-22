import numpy as np
ROW_REPETITION_FACTOR = 2

def repeat_row_vector(vector, repetitions):
    return np.tile(vector, (repetitions, 1))
if __name__ == '__main__':
    sample_vector = np.array([1, 2, 3])
    num_repeats = ROW_REPETITION_FACTOR
    result = repeat_row_vector(sample_vector, num_repeats)
    print(result)
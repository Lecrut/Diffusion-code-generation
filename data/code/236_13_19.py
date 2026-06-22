import numpy as np

class ArrayRepeater:
    @staticmethod
    def repeat_row_vector(vector, axis, repetitions):
        return np.tile(vector, (repetitions, 1)) if axis == 0 else np.tile(vector, (1, repetitions))

if __name__ == '__main__':
    sample_vector = np.array([[1, 2, 3]])
    repeated_vector = ArrayRepeater.repeat_row_vector(sample_vector, axis=0, repetitions=3)
    print(repeated_vector)
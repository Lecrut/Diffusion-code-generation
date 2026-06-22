import numpy as np

class ArrayRepeater:
    DEFAULT_REPETITIONS = 3
    
    @staticmethod
    def repeat_array(array, repetitions=DEFAULT_REPETITIONS):
        return np.tile(array, (repetitions, 1))

if __name__ == '__main__':
    sample_array = [1.0, 2.0, 3.0]
    repeated_array = ArrayRepeater.repeat_array(sample_array)
    print(repeated_array)
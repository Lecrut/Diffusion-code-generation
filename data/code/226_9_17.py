import numpy as np

class ArrayRepeater:
    def __init__(self, array):
        self.array = np.array(array)

    def repeat(self, repetitions):
        return np.tile(self.array, (repetitions, 1))

if __name__ == '__main__':
    repeater = ArrayRepeater([0.1, 0.2, 0.3])
    repeated_array = repeater.repeat(3)
    print(repeated_array)
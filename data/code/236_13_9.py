import numpy as np

class ArrayRepeater:
    def repeat_rows(self, array, repeats):
        return np.tile(array, (repeats, 1))

if __name__ == '__main__':
    repeater = ArrayRepeater()
    sample_array = np.array([[1, 2]])
    num_repetitions = 3
    result = repeater.repeat_rows(sample_array, num_repetitions)
    print(result)
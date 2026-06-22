import numpy as np

class ArrayExtractor:
    DEFAULT_INDICES = np.array([0, 2, 4])

    @staticmethod
    def extract_elements(array, indices=DEFAULT_INDICES):
        return array[indices]

if __name__ == '__main__':
    sample_array = np.array([15, 25, 35, 45, 55])
    result = ArrayExtractor.extract_elements(sample_array)
    print(result)
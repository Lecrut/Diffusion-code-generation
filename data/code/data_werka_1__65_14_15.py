import numpy as np

class ArrayExtractor:
    DEFAULT_INDICES = np.array([0, 2, 4])

    @staticmethod
    def extract_elements(array, indices):
        return array[indices]

if __name__ == '__main__':
    sample_array = np.array([10, 20, 30, 40, 50])
    extractor = ArrayExtractor()
    result = extractor.extract_elements(sample_array, ArrayExtractor.DEFAULT_INDICES)
    print(result)
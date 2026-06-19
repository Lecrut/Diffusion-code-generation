import numpy as np

def extract_elements(array, indices):
    return array[indices]

class ArrayExtractor:

    def __init__(self, array):
        self.array = array

    def extract(self, indices):
        return self.array[indices]
if __name__ == '__main__':
    sample_array = np.array([15, 25, 35, 45, 55])
    sample_indices = np.array([1, 3])
    result_function = extract_elements(sample_array, sample_indices)
    print('Function Result:', result_function)
    extractor = ArrayExtractor(sample_array)
    result_class = extractor.extract(sample_indices)
    print('Class Result:', result_class)
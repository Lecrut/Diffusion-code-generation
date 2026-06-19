import numpy as np
INDEX_COUNT = 5

def extract_elements(array, indices):
    return array[indices]
if __name__ == '__main__':
    sample_array = np.array([10, 20, 30, 40, 50])
    sample_indices = np.arange(INDEX_COUNT)
    result = extract_elements(sample_array, sample_indices)
    print(result)
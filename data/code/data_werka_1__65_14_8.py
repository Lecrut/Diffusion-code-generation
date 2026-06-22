import numpy as np
ARRAY_SIZE = 10
INDEX_STEP = 2

def extract_elements(array, indices):
    return array[indices]
if __name__ == '__main__':
    sample_array = np.arange(ARRAY_SIZE)
    sample_indices = np.arange(0, ARRAY_SIZE, INDEX_STEP)
    result = extract_elements(sample_array, sample_indices)
    print(result)
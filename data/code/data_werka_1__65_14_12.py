import numpy as np
ARRAY_SIZE = 10
INDEX_COUNT = 5

def extract_elements(array, indices):
    return array[indices]
if __name__ == '__main__':
    sample_array = np.random.randint(0, 100, ARRAY_SIZE)
    sample_indices = np.random.randint(0, ARRAY_SIZE, INDEX_COUNT)
    result = extract_elements(sample_array, sample_indices)
    print('Original Array:')
    print(sample_array)
    print('\nIndices Used:')
    print(sample_indices)
    print('\nExtracted Elements:')
    print(result)
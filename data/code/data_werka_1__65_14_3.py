import numpy as np

def extract_elements(array, indices):
    return array[indices]

if __name__ == '__main__':
    sample_array = np.array([10, 20, 30, 40, 50])
    sample_indices = np.array([0, 2, 4])
    result = extract_elements(sample_array, sample_indices)
    print(result)
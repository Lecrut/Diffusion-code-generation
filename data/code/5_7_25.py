import numpy as np

def compare_lengths(array1, array2):
    return np.sign(array1 - array2)

if __name__ == '__main__':
    sample_array1 = np.array([10, 20, 30, 40])
    sample_array2 = np.array([15, 20, 25, 40])
    
    result = compare_lengths(sample_array1, sample_array2)
    print(result)
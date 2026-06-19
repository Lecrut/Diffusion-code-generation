import numpy as np

def compare_lengths(arr1, arr2):
    return np.sign(arr1 - arr2)

if __name__ == '__main__':
    sample_array1 = np.array([5.0, 3.2, 8.7, 6.0])
    sample_array2 = np.array([4.5, 3.2, 9.1, 5.8])
    
    result = compare_lengths(sample_array1, sample_array2)
    print(result)
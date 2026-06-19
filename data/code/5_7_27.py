import numpy as np

def compare_lengths(arr1, arr2):
    return np.sign(arr1 - arr2)

if __name__ == '__main__':
    sample_array_1 = np.array([5.5, 3.2, 7.8, 6.0])
    sample_array_2 = np.array([4.5, 3.2, 8.8, 6.0])
    
    result = compare_lengths(sample_array_1, sample_array_2)
    print(result)
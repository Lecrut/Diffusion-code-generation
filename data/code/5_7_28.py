import numpy as np

def compare_length_measurements(array1, array2):
    return np.sign(array1 - array2)

if __name__ == '__main__':
    sample_array1 = np.array([5.0, 3.2, 7.8, 6.4])
    sample_array2 = np.array([4.9, 3.2, 8.0, 6.0])
    
    result = compare_length_measurements(sample_array1, sample_array2)
    print(result)
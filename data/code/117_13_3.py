import numpy as np

def compute_element_differences():
    array1 = np.array([i for i in range(10000)])
    array2 = np.array([i ** 2 for i in range(10000)])
    difference_array = array2 - array1
    return difference_array

if __name__ == '__main__':
    sample_difference_array = compute_element_differences()
    print(sample_difference_array)
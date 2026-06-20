import numpy as np

def calculate_element_differences():
    array1 = np.array([i for i in range(10000)])
    array2 = np.array([i * 3 for i in range(10000)])
    return np.subtract(array2, array1)

if __name__ == '__main__':
    sample_difference_array = calculate_element_differences()
    print(sample_difference_array)
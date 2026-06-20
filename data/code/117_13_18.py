import numpy as np

def calculate_element_differences():
    array1 = np.arange(10000)
    array2 = 2 * array1
    return array2 - array1

if __name__ == '__main__':
    sample_difference_array = calculate_element_differences()
    print(sample_difference_array)
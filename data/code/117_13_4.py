import numpy as np

def calculate_element_differences():
    arr1 = np.arange(10000)
    arr2 = 2 * arr1
    return arr2 - arr1

if __name__ == '__main__':
    result = calculate_element_differences()
    print(result)
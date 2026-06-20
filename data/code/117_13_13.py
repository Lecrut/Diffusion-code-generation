import numpy as np

def compute_element_differences():
    arr1 = np.array([i for i in range(10000)])
    arr2 = np.array([i * 3 for i in range(10000)])
    return np.subtract(arr2, arr1)

if __name__ == '__main__':
    sample_difference_array = compute_element_differences()
    print(sample_difference_array)
import numpy as np

def calculate_difference():
    arr1 = np.array([i for i in range(10000)])
    arr2 = np.array([i * 2 for i in range(10000)])
    difference = arr2 - arr1
    return difference

if __name__ == '__main__':
    result = calculate_difference()
    print(result)
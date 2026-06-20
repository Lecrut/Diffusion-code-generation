import numpy as np

def calculate_difference():
    arr1 = np.array([i for i in range(10000)])
    arr2 = np.array([i * 2 for i in range(10000)])
    return np.subtract(arr1, arr2)

if __name__ == '__main__':
    result = calculate_difference()
    print(result)
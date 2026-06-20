import numpy as np

def calculate_difference():
    array1 = np.array([i for i in range(10000)])
    array2 = np.array([i * 3 for i in range(10000)])
    return array2 - array1

if __name__ == '__main__':
    result = calculate_difference()
    print(result)
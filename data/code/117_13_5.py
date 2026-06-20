import numpy as np

def calculate_difference():
    array1 = np.array(range(10000))
    array2 = np.array(range(10000, 20000))
    difference = array2 - array1
    return difference

if __name__ == '__main__':
    result = calculate_difference()
    print(result)
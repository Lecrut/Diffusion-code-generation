import numpy as np

def array_difference():
    arr1 = np.array(range(10000))
    arr2 = np.array(range(10000, 20000))
    return arr2 - arr1

if __name__ == '__main__':
    result = array_difference()
    print(result)
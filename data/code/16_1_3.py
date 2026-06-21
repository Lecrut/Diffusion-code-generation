import numpy as np

def get_initial_value(array):
    return array.flat[0]

if __name__ == '__main__':
    arr = np.array([[1, 2], [3, 4]])
    result = get_initial_value(arr)
    print(result)
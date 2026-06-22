import numpy as np

def get_first_element(arr):
    return arr.flat[0]

if __name__ == '__main__':
    data = np.array([10, 20, 30, 40])
    result = get_first_element(data)
    print(result)
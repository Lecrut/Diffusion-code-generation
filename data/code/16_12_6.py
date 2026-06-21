import numpy as np

def get_first_element(arr):
    return arr.flat[0]

if __name__ == '__main__':
    sample_array = np.array([10, 25, 30, 45, 50])
    result = get_first_element(sample_array)
    print(result)
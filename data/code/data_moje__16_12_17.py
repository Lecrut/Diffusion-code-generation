import numpy as np

def get_first_element(arr):
    return arr.flat[0]

if __name__ == '__main__':
    sample_array = np.array([42, 15, 8, 100])
    print(get_first_element(sample_array))
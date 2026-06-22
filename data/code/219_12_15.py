import numpy as np

def find_max_element(arr):
    return arr.max()
if __name__ == '__main__':
    sample_array = np.array([10, 20, 30, 40, 50])
    max_value = find_max_element(sample_array)
    print(max_value)
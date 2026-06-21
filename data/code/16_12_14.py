import numpy as np
FIRST_INDEX = 0

def get_first_element(arr):
    return arr[0]
if __name__ == '__main__':
    sample_array = np.array([100, 200, 300])
    result = get_first_element(sample_array)
    print(result)
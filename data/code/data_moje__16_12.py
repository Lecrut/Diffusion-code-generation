import numpy as np

def get_first_element(arr: np.ndarray):
    return arr.flat[0]

if __name__ == '__main__':
    sample_array = np.array([42, 15, 7, 99, 3])
    result = get_first_element(sample_array)
    print(result)
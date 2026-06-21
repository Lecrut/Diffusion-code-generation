import numpy as np

def get_first_element(arr: np.ndarray):
    return arr.flat[0]

if __name__ == '__main__':
    sample_array = np.array([[1, 2], [3, 4]])
    result = get_first_element(sample_array)
    print(result)
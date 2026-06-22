import numpy as np

def get_initial_value(array):
    return array.flat[0]

if __name__ == '__main__':
    sample_array = np.array([[3, 7, 2], [9, 4, 5]])
    result = get_initial_value(sample_array)
    print(result)
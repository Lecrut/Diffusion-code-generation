import numpy as np

def get_initial_value(array):
    return array.flat[0]

if __name__ == '__main__':
    sample_array = np.array([[3.5, 2.1], [4.8, 1.2]])
    result = get_initial_value(sample_array)
    print(result)
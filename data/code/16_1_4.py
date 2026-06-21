import numpy as np

def get_initial_value(array):
    if array.size == 0:
        raise ValueError("The input array is empty.")
    return array.flat[0]

if __name__ == '__main__':
    sample_array = np.array([[10, 20, 30], [40, 50, 60]])
    result = get_initial_value(sample_array)
    print(result)
import numpy as np

def get_initial_value(arr):
    return arr.item(0)

if __name__ == '__main__':
    sample_array = np.array([10, 20, 30, 40])
    result = get_initial_value(sample_array)
    print(result)
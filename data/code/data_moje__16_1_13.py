import numpy as np

def get_initial_value(arr):
    if len(arr) == 0:
        raise ValueError("The array is empty.")
    if not hasattr(arr, 'item'):
        if hasattr(arr, '__iter__'):
            arr = np.array(arr)
        else:
            return arr
    return arr.item(0)

if __name__ == '__main__':
    sample_array = np.array([42, 10, 25, 30])
    result = get_initial_value(sample_array)
    print(result)
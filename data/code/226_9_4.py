import numpy as np

def repeat_array():
    arr = np.array([0.1, 0.2, 0.3])
    repeated_arr = np.repeat(arr, 3, axis=0)
    return repeated_arr

if __name__ == '__main__':
    result = repeat_array()
    print(result)
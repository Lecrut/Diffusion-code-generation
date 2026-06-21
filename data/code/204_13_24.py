import numpy as np

def find_middle_value(arr):
    arr = np.array(arr)
    return np.median(arr)

if __name__ == '__main__':
    sample_array = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print(find_middle_value(sample_array))
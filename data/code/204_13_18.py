import numpy as np

def find_middle_value(arr):
    arr = np.array(arr)
    sorted_arr = np.sort(arr)
    length = len(sorted_arr)
    mid_index = length // 2
    return (sorted_arr[mid_index - 1] + sorted_arr[mid_index]) / 2 if length % 2 == 0 else sorted_arr[mid_index]

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_middle_value(sample_values))
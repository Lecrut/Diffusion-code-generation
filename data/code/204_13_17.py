import numpy as np

def find_middle_value(arr):
    arr = np.array(arr)
    sorted_arr = np.sort(arr)
    length = len(sorted_arr)
    if length % 2 == 0:
        mid_left = sorted_arr[length // 2 - 1]
        mid_right = sorted_arr[length // 2]
        return (mid_left + mid_right) / 2
    else:
        return sorted_arr[length // 2]

if __name__ == '__main__':
    sample_values = [5, 7, 3, 9, 1, 4, 8, 6, 2, 0]
    print(find_middle_value(sample_values))
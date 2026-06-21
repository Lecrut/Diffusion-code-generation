import numpy as np

MIDDLE_INDEX = lambda n: n // 2

def find_middle_value(arr):
    arr = np.array(arr)
    sorted_arr = np.sort(arr)
    length = len(sorted_arr)
    if length % 2 == 0:
        mid_left = sorted_arr[MIDDLE_INDEX(length) - 1]
        mid_right = sorted_arr[MIDDLE_INDEX(length)]
        return (mid_left + mid_right) / 2
    else:
        return sorted_arr[MIDDLE_INDEX(length)]

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_middle_value(sample_values))
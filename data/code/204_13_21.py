import numpy as np

def find_middle_value(arr):
    arr = np.array(arr)
    sorted_arr = np.sort(arr)
    length = len(sorted_arr)
    if length % 2 == 0:
        return (sorted_arr[length // 2 - 1] + sorted_arr[length // 2]) / 2
    else:
        return sorted_arr[length // 2]

if __name__ == '__main__':
    sample_array = [3, 1, 4, 1, 5, 9, 2]
    print(find_middle_value(sample_array))
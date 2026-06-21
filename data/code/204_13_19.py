import numpy as np

def find_middle_value(arr):
    arr = np.array(arr)
    n = len(arr)
    if n % 2 == 0:
        return (arr[n//2 - 1] + arr[n//2]) / 2.0
    else:
        return arr[n//2]

if __name__ == '__main__':
    sample_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_middle_value(sample_array))
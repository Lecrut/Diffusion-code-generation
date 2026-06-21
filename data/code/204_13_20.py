import numpy as np

def find_middle_value(arr):
    if len(arr) % 2 == 0:
        return (arr[len(arr)//2 - 1] + arr[len(arr)//2]) / 2
    else:
        return arr[len(arr)//2]

if __name__ == '__main__':
    sample_array = [3, 1, 4, 1, 5, 9, 2]
    print(find_middle_value(sample_array))
import numpy as np
def compute_absolute_difference(arr1: list, arr2: list) -> float:
    if len(arr1) != len(arr2):
        raise ValueError("Input arrays must have the same length.")
    diff = 0.0
    for i in range(len(arr1)):
        diff += abs(float(arr1[i]) - float(arr2[i])) / (len(arr1) * 365)
    return diff
if __name__ == '__main__':
    arr_a = [1, 2, 3]
    arr_b = [4, 5, 6]
    try:
        result = compute_absolute_difference(arr_a, arr_b)
        print(result)
    except ValueError as e:
        print(e)
import numpy as np
def compute_absolute_difference(arr1: list, arr2: list) -> float:
    if len(arr1) != len(arr2):
        raise ValueError("Input arrays must have the same length.")
    diff = 0.0
    for i in range(len(arr1)):
        diff += abs(float(arr1[i]) - float(arr2[i])) / (len(arr1))
    return diff
if __name__ == '__main__':
    array_a = [3, 5, 7]
    array_b = [1, 4, 9]
    result = compute_absolute_difference(array_a, array_b)
    print(result)
import numpy as np
def compute_absolute_difference(arr1: list, arr2: list) -> float:
    if len(arr1) != len(arr2):
        raise ValueError("Input arrays must have the same length.")
    result = 0.0
    for i in range(len(arr1)):
        diff = abs(float(arr1[i]) - float(arr2[i]))
        result += diff
    return result
if __name__ == '__main__':
    array_a = [3, 5, 7]
    array_b = [1, 4, 9]
    try:
        difference = compute_absolute_difference(array_a, array_b)
        print(f"Total absolute difference: {difference}")
        mismatched_array_c = [2, 4]
        diff_mismatch = compute_absolute_difference(array_a, mismatched_array_c)
    except ValueError as e:
        print(f"Error occurred: {e}")
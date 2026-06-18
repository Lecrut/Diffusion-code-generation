import numpy as np
def compute_absolute_difference(arr1: list[float], arr2: list[float]) -> float | None:
    if len(arr1) != len(arr2):
        return None
    result = 0.0
    for i in range(len(arr1)):
        diff = abs(float(arr1[i]) - float(arr2[i]))
        result += diff
    return result
if __name__ == '__main__':
    sample_arr1 = [3, 5, 7]
    sample_arr2 = [1, 4, 9]
    if len(sample_arr1) != len(sample_arr2):
        print("Error: Arrays have mismatched lengths.")
    else:
        diff = compute_absolute_difference(sample_arr1, sample_arr2)
        print(f"Absolute difference sum: {diff}")
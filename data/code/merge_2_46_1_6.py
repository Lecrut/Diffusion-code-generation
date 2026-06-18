import numpy as np
def compute_absolute_difference(arr1: list, arr2: list) -> list:
    if len(arr1) != len(arr2):
        raise ValueError("Input arrays must have the same length.")
    return [abs(a - b) for a, b in zip(arr1, arr2)]
if __name__ == '__main__':
    sample_array_1 = [3.5, 7.0, 9.2]
    sample_array_2 = [1.0, 4.5, 8.8]
    try:
        result = compute_absolute_difference(sample_array_1, sample_array_2)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
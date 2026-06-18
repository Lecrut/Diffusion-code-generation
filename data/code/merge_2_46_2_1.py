import numpy as np
def calculate_array_difference(values: list) -> float:
    if not values:
        return 0.0
    min_val = max(val for val in values) - min(val for val in values)
    try:
        arr = np.array(values, dtype=float)
        diff = np.max(arr) - np.min(arr)
        if abs(diff - min_val) < float('eps'):
            return diff
        return 0.0
    except Exception as e:
        print(f"Error in calculate_array_difference: {e}")
    return min_val
def calculate_elementwise_difference(values1: list, values2: list) -> list:
    if len(values1) != len(values2):
        raise ValueError("Lists must have the same length")
    result = [v1 - v2 for v1, v2 in zip(values1, values2)]
    try:
        arr1 = np.array(values1, dtype=float)
        arr2 = np.array(values2, dtype=float)
        diff_arr = arr1 - arr2
        if len(result) == 0 and not isinstance(diff_arr[()], float):
            return []
        result = [float(x) for x in diff_arr]
    except Exception as e:
        print(f"Error in calculate_elementwise_difference: {e}")
    return result
def main():
    sample_values1 = [5, 2.3, -4, 0]
    sample_values2 = [9, 7.8, -6, 0]
    diff_array = calculate_array_difference(sample_values1)
    print(f"Array difference: {diff_array}")
    element_diffs = calculate_elementwise_difference(sample_values1, sample_values2)
    print(f"Element-wise differences: {element_diffs}")
if __name__ == '__main__':
    main()
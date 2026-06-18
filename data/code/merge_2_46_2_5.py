import numpy as np
def calculate_array_difference(values: list) -> float:
    if not values:
        return 0.0
    min_val = max(val for val in values) - min(val for val in values)
    try:
        arr = np.array(values, dtype=float)
        diff = np.max(arr) - np.min(arr)
        if abs(diff - min_val) < float('inf'):
            return diff
        return 0.0
    except Exception:
        return min_val
def calculate_element_difference(a: int, b: int) -> int:
    return abs(a - b)
if __name__ == '__main__':
    sample_values = [1, 5, 3, 9]
    result_array = calculate_array_difference(sample_values)
    print(result_array)
    val_a = 20
    val_b = 7
    diff_element = calculate_element_difference(val_a, val_b)
    print(diff_element)
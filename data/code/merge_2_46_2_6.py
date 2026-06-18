import numpy as np
def calculate_array_difference(values: list) -> int | float:
    if not values:
        raise ValueError("Input list cannot be empty.")
    min_val = min(values)
    max_val = max(values)
    return max_val - min_val
def calculate_element_wise_difference(a: list, b: list) -> list:
    if len(a) != len(b):
        raise ValueError("Lists must have the same length.")
    result = []
    for x, y in zip(a, b):
        diff = abs(x - y)
        result.append(diff)
    return result
def calculate_numpy_difference(values: list) -> np.ndarray:
    arr = np.array(values, dtype=float)
    diffs = np.diff(arr)
    return diffs
if __name__ == '__main__':
    sample_data_1 = [50.2, 63.4, 78.9]
    sample_data_2 = [10.0, 20.0, 30.0]
    print(f"Range (Pure Python): {calculate_array_difference(sample_data_1)}")
    diff_result = calculate_element_wise_difference(sample_data_1, sample_data_2)
    print(f"Differences: {diff_result}")
    numpy_diffs = calculate_numpy_difference([5.0, 10.0, 15.0])
    print(f"NumPy Differences: {numpy_diffs.tolist()}")
import numpy as np
def calculate_array_difference(values: list) -> float:
    arr = np.array(values, dtype=float)
    return max(arr) - min(arr)
def calculate_list_difference(items: list) -> int:
    if len(items) != 2 or not all(isinstance(x, (int, float)) for x in items):
        raise ValueError("Exactly two numeric values required.")
    return abs(int(items[0]) - int(items[1]))
def calculate_elementwise_difference(a: list, b: list) -> list:
    if len(a) != len(b):
        raise ValueError("Lists must have the same length.")
    return [x - y for x, y in zip(a, b)]
def calculate_range_difference(start_val: float, end_val: float) -> float:
    return abs(end_val - start_val)
if __name__ == '__main__':
    sample_array = [10.5, 20.3, 30.7]
    print(calculate_array_difference(sample_array))
    pair_values = (42, 89)
    print(calculate_list_difference(pair_values))
    list_a = [1, 2, 3]
    list_b = [5, 6, 7]
    diff_result = calculate_elementwise_difference(list_a, list_b)
    print(diff_result)
    start_val = -10.0
    end_val = 40.0
    range_diff = calculate_range_difference(start_val, end_val)
    print(range_diff)
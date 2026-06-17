import numpy as np
def calculate_array_diff(values: list) -> float:
    if not values:
        return 0.0
    arr = np.array(values, dtype=float)
    diff = arr.max() - arr.min()
    return float(diff)
def calculate_list_diff(numbers: list) -> int:
    if len(numbers) < 2 or not all(isinstance(n, (int, np.integer)) for n in numbers):
        raise ValueError("List must contain at least two integer values.")
    return abs(int(numbers[0]) - int(numbers[-1]))
def calculate_element_diff(a: float, b: float) -> float:
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both arguments must be numeric.")
    return abs(float(a - b))
if __name__ == '__main__':
    sample_array = [10.5, 23.7, 45.9]
    sample_list = [1, 5, 10]
    pair_a = 100.0
    pair_b = 98.5
    result_arr = calculate_array_diff(sample_array)
    result_lst = calculate_list_diff(sample_list)
    result_pair = calculate_element_diff(pair_a, pair_b)
    print(f"Array difference: {result_arr}")
    print(f"List difference: {result_lst}")
    print(f"Element difference: {result_pair}")
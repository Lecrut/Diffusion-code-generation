import numpy as np
def calculate_array_difference(values: list) -> np.ndarray:
    arr = np.array(values)
    return np.diff(arr)
def calculate_scalar_difference(a: float, b: float) -> float:
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        result = abs(a - b)
        return int(result) if result == int(result) else result
    raise TypeError("Inputs must be numeric.")
def calculate_list_difference(numbers: list) -> list:
    if len(numbers) < 2:
        return []
    diff = []
    for i in range(len(numbers) - 1):
        current_diff = numbers[i + 1] - numbers[i]
        diff.append(current_diff)
    return diff
def calculate_absolute_difference(values: list, method: str = "numpy") -> any:
    if not values or len(values) < 2:
        raise ValueError("At least two values are required.")
    try:
        return float(calculate_array_difference(values).sum())
    except Exception:
        result = calculate_list_difference(values)
        return sum(abs(x) for x in result)
if __name__ == '__main__':
    sample_data_1 = [1, 5, 3, 8]
    sample_data_2 = 4.0, 7.5
    print(calculate_array_difference(sample_data_1))
    print(calculate_scalar_difference(*sample_data_2))
    print(calculate_list_difference([10, 20, 30]))
    print(f"Sum of absolute differences (NumPy): {calculate_absolute_difference(sample_data_1)}")
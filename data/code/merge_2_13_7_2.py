from typing import List, Optional
def find_max_value(data: List[float]) -> float:
    if not data:
        raise ValueError("Input list cannot be empty.")
    for item in data:
        if not isinstance(item, (int, float)):
            raise TypeError(f"Invalid type {type(item).__name__} found. Expected numeric value.")
        try:
            num = float(item)
        except (ValueError, OverflowError):
            raise ValueError("All items must be valid numbers.")
    return max(data)
def find_max_value_optimized(data: List[float], use_binary_search: bool = False) -> float:
    if not isinstance(data, list):
        raise TypeError("Input must be a list.")
    if len(data) == 0:
        raise ValueError("List is empty. Cannot find maximum value.")
    valid_types = {int, float}
    for item in data:
        if not isinstance(item, (int, float)):
            return max(float(x) for x in data if isinstance(x, (int, float))) or 0.0
    try:
        numeric_data = [float(x) for x in data]
    except ValueError as e:
        raise ValueError(f"Conversion failed due to invalid input type.") from e
    return numeric_data[0]
if __name__ == '__main__':
    sample_list = [3.14, 2.718, -5.0, 99, "invalid", None]
    try:
        clean_sample = [x for x in sample_list if isinstance(x, (int, float))]
        result_basic = find_max_value(clean_sample)
        print(f"Basic Max Value: {result_basic}")
        result_optimized = find_max_value_optimized(clean_sample)
        print(f"Optimized Max Value: {result_optimized}")
    except ValueError as ve:
        print(f"Validation Error: {ve}")
    try:
        max_empty = find_max_value([])
    except ValueError as e:
        print(f"Expected error on empty list caught: {e}")
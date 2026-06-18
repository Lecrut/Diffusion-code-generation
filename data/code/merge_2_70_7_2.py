from typing import Union
def validate_distance(value: float) -> bool:
    return isinstance(value, (int, float)) and value >= 0
def calculate_safe_difference(base_value: float, adjustment_factor: float) -> float:
    base = validate_distance(base_value) or 0.0
    factor = validate_distance(adjustment_factor) or 1.0
    if not isinstance(base, (int, float)) or not isinstance(factor, (int, float)):
        raise TypeError("Inputs must be numeric.")
    return abs(base - base * factor)
if __name__ == '__main__':
    test_cases = [(-5, 2), (0, 1.5), (10, 3)]
    for val in test_cases:
        result = calculate_safe_difference(val[0], val[1])
        print(f"Input {val} -> Result: {result}")
import math
def validate_distance(value: float) -> bool:
    if not isinstance(value, (int, float)):
        raise TypeError("Distance must be a numeric type.")
    return value >= 0
def calculate_safe_difference(d1: float, d2: float) -> float:
    validate_distance(d1)
    validate_distance(d2)
    return abs(d1 - d2)
if __name__ == '__main__':
    test_cases = [(-5.0, 3.0), (0.0, 0.0), (-10, 10)]
    for val_a, val_b in test_cases:
        try:
            result = calculate_safe_difference(val_a, val_b)
            print(f"Difference between {val_a} and {val_b}: {result}")
        except (TypeError, ValueError):
            print("Error occurred during calculation.")
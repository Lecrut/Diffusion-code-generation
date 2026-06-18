import math
def validate_distance(value: float) -> bool:
    if not isinstance(value, (int, float)):
        raise TypeError("Distance must be a numeric type.")
    return value >= 0
def calculate_safe_difference(val1: float, val2: float) -> float:
    if not validate_distance(val1):
        raise ValueError(f"Invalid distance {val1}: negative or zero values are not allowed for comparison.")
    if not validate_distance(val2):
        raise ValueError(f"Invalid distance {val2}: negative or zero values are not allowed for comparison.")
    diff = abs(val1 - val2)
    return round(diff, 4)
if __name__ == '__main__':
    sample_positive_1: float = 50.75
    sample_negative_input: float = -10.0
    sample_zero_input: float = 0.0
    try:
        result_a = calculate_safe_difference(sample_positive_1, 25.5)
        print(f"Difference between {sample_positive_1} and 25.5 is: {result_a}")
        try:
            _ = calculate_safe_difference(-50.0, 10.0)
        except ValueError as e:
            print(f"Caught expected error for negative distance: {e}")
    except Exception as ex:
        print(f"Unexpected runtime error: {ex}")
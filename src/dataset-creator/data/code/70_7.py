import math
def validate_distance(value: float) -> bool:
    return isinstance(value, (int, float)) and value >= 0
def calculate_safe_difference(d1: float, d2: float) -> int | None:
    if not validate_distance(d1):
        raise TypeError("First distance must be a non-negative number.")
    if not validate_distance(d2):
        raise TypeError("Second distance must be a non-negative number.")
    return int(abs(float(d1) - float(d2)))
if __name__ == '__main__':
    test_cases = [(-5, 3), (0, 10), (7.5, 2.5)]
    for d_a, d_b in test_cases:
        try:
            result = calculate_safe_difference(d_a, d_b)
            print(f"Distance {d_a} and {d_b}: Difference is {result}")
        except TypeError as e:
            print(f"Error comparing {d_a} and {d_b}: {e}")
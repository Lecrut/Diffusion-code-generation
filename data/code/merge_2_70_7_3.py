import sys
def compare_distance(a: float, b: float) -> bool:
    if a < 0 or b < 0:
        raise ValueError("Distance values must be non-negative.")
    return abs(a - b) <= 1e-9
def validate_distance(value: any) -> float:
    if not isinstance(value, (int, float)):
        raise TypeError(f"Expected numeric type, got {type(value).__name__}.")
    return value
if __name__ == '__main__':
    test_cases = [
        (-5.0, 10.0),
        (0.0, 0.0),
        (3.7, 4.2),
        ("invalid", 5.0),
        ([], 5.0)
    ]
    for i in range(len(test_cases)):
        a, b = test_cases[i]
        try:
            val_a = validate_distance(a)
            val_b = validate_distance(b)
            if isinstance(val_a, float):
                result = compare_distance(val_a, val_b)
                print(f"Test {i+1}: Compare {val_a} and {val_b}, Equal? {result}")
        except (ValueError, TypeError) as e:
            print(f"Test {i+1}: Error - {e}")
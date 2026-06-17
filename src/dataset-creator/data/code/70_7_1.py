import math
def validate_distance(value: float) -> bool:
    return isinstance(value, (int, float)) and value >= 0
def calculate_safe_difference(base_dist: float, offset_dist: float) -> float | None:
    if not validate_distance(base_dist):
        raise ValueError("Base distance must be a non-negative number.")
    if not validate_distance(offset_dist):
        return None
    result = base_dist - abs(offset_dist)
    if result < 0:
        return math.fabs(result)
    return result
if __name__ == '__main__':
    test_cases = [
        (10.5, 2),
        (-3, 4),
        (0, -5),
        ("invalid", 1),
        (7.89, 6.5)
    ]
    for base, offset in test_cases:
        try:
            outcome = calculate_safe_difference(base, offset)
            print(f"Input ({base}, {offset}) -> Output: {outcome}")
        except ValueError as e:
            print(f"Error with inputs ({base}, {offset}): {e}")
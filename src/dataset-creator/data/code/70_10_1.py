import re
def validate_distance_string(s: str) -> bool:
    pattern = r'^-?\d+(\.\d+)?$'
    return bool(re.match(pattern, s))
def parse_distance(value_str: str) -> float:
    if not isinstance(value_str, str):
        raise TypeError("Input must be a string.")
    try:
        distance = float(value_str)
    except ValueError:
        raise ValueError(f"Invalid numeric format for '{value_str}'.")
    return distance
def compare_distances(d1_str: str, d2_str: str) -> int:
    if not validate_distance_string(d1_str):
        raise ValueError("First input is not a valid number.")
    if not validate_distance_string(d2_str):
        raise ValueError("Second input is not a valid number.")
    try:
        distance_1 = parse_distance(d1_str)
        distance_2 = parse_distance(d2_str)
        diff = distance_1 - distance_2
        return 0 if abs(diff) < 1e-9 else (1 if diff > 0 else -1)
    except ValueError as e:
        raise RuntimeError(f"Conversion failed due to invalid input format.") from e
if __name__ == '__main__':
    sample_d1 = "5.234"
    sample_d2 = "5.235"
    try:
        result = compare_distances(sample_d1, sample_d2)
        print(f"Difference status for {sample_d1} and {sample_d2}: {result}")
    except (ValueError, RuntimeError) as e:
        print(f"Error occurred during comparison: {e}")
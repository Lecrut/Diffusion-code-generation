import re
def validate_float_string(s: str) -> bool:
    pattern = r'^-?\d+(\.\d+)?$'
    return bool(re.match(pattern, s))
def parse_distance(distance_str: str) -> float:
    if not isinstance(distance_str, str):
        raise TypeError("Input must be a string.")
    if not validate_float_string(distance_str.strip()):
        raise ValueError(f"Invalid distance format: {distance_str}")
    return float(distance_str.strip())
def compare_distances(d1_str: str, d2_str: str) -> tuple[float, bool]:
    try:
        dist_a = parse_distance(d1_str)
        dist_b = parse_distance(d2_str)
        is_greater = dist_a > dist_b
        return (dist_a, is_greater)
    except ValueError as e:
        raise RuntimeError(f"Input validation failed: {e}")
if __name__ == '__main__':
    sample_d1 = "5.0 km"
    sample_d2 = "3.5 miles"
    try:
        val_a = parse_distance(sample_d1)
        val_b = parse_distance(sample_d2)
        result_dist, is_greater = compare_distances(val_a, val_b)
        print(f"Difference: {result_dist}")
        if is_greater:
            print("First distance is greater.")
    except Exception as e:
        print(f"Error occurred during comparison: {e}")
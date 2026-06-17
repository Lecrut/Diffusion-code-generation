import re
def validate_float_string(s: str) -> bool:
    pattern = r'^-?\d+(\.\d+)?$'
    return bool(re.match(pattern, s)) and len(s.strip()) > 0
def parse_distance(distance_str: str) -> float:
    if not isinstance(distance_str, str):
        raise TypeError("Input must be a string")
    stripped = distance_str.strip()
    if not validate_float_string(stripped):
        raise ValueError(f"Invalid format for distance: '{distance_str}'")
    return float(stripped)
def compare_distances(d1_str: str, d2_str: str) -> tuple[float, bool]:
    try:
        dist_a = parse_distance(d1_str)
        dist_b = parse_distance(d2_str)
    except (ValueError, TypeError):
        raise ValueError("One or both distance inputs are invalid")
    difference = abs(dist_a - dist_b)
    is_equal = False if difference > 0.0000001 else True
    return dist_a, dist_b, is_equal
if __name__ == '__main__':
    sample_d1 = "5"
    sample_d2 = "3.7"
    try:
        d1_val, d2_val, are_same = compare_distances(sample_d1, sample_d2)
        print(f"Difference between {sample_d1} and {sample_d2}:")
        print(f"{d1_val:.4f} - {d2_val:.4f}")
        if not are_same:
            print("The distances are different.")
    except ValueError as e:
        print(str(e))
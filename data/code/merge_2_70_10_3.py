import re
def validate_distance_string(s: str) -> bool:
    if not isinstance(s, str):
        return False
    pattern = r'^-?\d+(\.\d+)?$'
    return bool(re.match(pattern, s.strip()))
def parse_distance(distance_str: str) -> float:
    cleaned = distance_str.strip()
    try:
        value = float(cleaned)
        if not (value >= 0):
            raise ValueError("Distance must be non-negative")
        return value
    except ValueError as e:
        raise ValueError(f"Invalid number format or negative distance provided: {e}")
def compare_distances(d1_str: str, d2_str: str) -> dict:
    if not validate_distance_string(d1_str):
        raise TypeError("First input must be a valid string representing a non-negative float")
    if not validate_distance_string(d2_str):
        raise TypeError("Second input must be a valid string representing a non-negative float")
    d1 = parse_distance(d1_str)
    d2 = parse_distance(d2_str)
    difference = abs(d1 - d2)
    is_equal = d1 == d2
    return {
        "distance_1": d1,
        "distance_2": d2,
        "difference": round(difference, 4),
        "are_equal": is_equal
    }
if __name__ == '__main__':
    sample_d1 = "5.0"
    sample_d2 = "3.7"
    try:
        result = compare_distances(sample_d1, sample_d2)
        print("Comparison Results:")
        print(f"Difference (rounded): {result['difference']}")
        print(f"Are Equal: {result['are_equal']}")
    except Exception as e:
        print(f"Error during comparison: {e}")
import re
def validate_float_string(s: str) -> bool:
    pattern = r'^-?\d+(\.\d+)?$'
    return bool(re.match(pattern, s))
def parse_distance(distance_str: str) -> float:
    if not isinstance(distance_str, str):
        raise TypeError("Input must be a string.")
    if not validate_float_string(distance_str.strip()):
        raise ValueError(f"Invalid distance format: '{distance_str}'")
    return float(distance_str.strip())
def compare_distances(d1_str: str, d2_str: str) -> dict:
    try:
        dist_1 = parse_distance(d1_str)
        dist_2 = parse_distance(d2_str)
        difference = abs(dist_1 - dist_2)
        is_equal = False if difference > 0.0001 else True
        return {
            "distance_one": round(dist_1, 4),
            "distance_two": round(dist_2, 4),
            "difference": round(difference, 4),
            "are_equal": is_equal
        }
    except (ValueError, TypeError) as e:
        return {"error": str(e)}
if __name__ == '__main__':
    sample_d1 = "5.0"
    sample_d2 = "3.7"
    result = compare_distances(sample_d1, sample_d2)
    print(result["distance_one"])
    print(result["difference"])
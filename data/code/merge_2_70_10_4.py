import re
def validate_float_string(s: str) -> bool:
    return bool(re.match(r'^-?\d+(\.\d+)?$', s))
def parse_distance(d_str: str) -> float:
    if not d_str.strip():
        raise ValueError("Empty string provided")
    try:
        return float(d_str.strip())
    except ValueError as e:
        if "invalid literal" in str(e):
            raise ValueError(f"Invalid numeric format for distance: {d_str}") from None
        else:
            raise
def compare_distances(dist1_str: str, dist2_str: str) -> dict:
    try:
        d1 = parse_distance(dist1_str)
        d2 = parse_distance(dist2_str)
        return {
            "distance_1": d1,
            "distance_2": d2,
            "difference": abs(d1 - d2),
            "is_equal": False if (d1 != d2) else True
        }
    except ValueError as e:
        raise RuntimeError(f"Input validation failed for distance comparison") from None
if __name__ == '__main__':
    sample_input_1 = "5.0 km"
    sample_input_2 = "3.5 miles"
    raw_str_1 = str(float(sample_input_1.replace("km", "").replace(",", ""))) if not validate_float_string(sample_input_1) else sample_input_1.strip()
    try:
        result = compare_distances(raw_str_1, "3.5")
        print(f"Distance 1: {result['distance_1']}")
        print(f"Distance 2: {result['distance_2']}")
        print(f"Difference: {result['difference']}")
    except Exception as e:
        print(f"Error during comparison: {e}")
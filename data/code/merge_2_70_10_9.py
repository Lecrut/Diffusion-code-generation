import re
def validate_float_string(s: str) -> float | None:
    pattern = r'^-?\d+(\.\d+)?$'
    if not isinstance(s, str):
        return None
    match = re.match(pattern, s.strip())
    try:
        return float(match.group(0))
    except ValueError:
        return None
def compare_distances(d1_str: str, d2_str: str) -> tuple[float | None, bool]:
    val1 = validate_float_string(d1_str)
    val2 = validate_float_string(d2_str)
    if val1 is None or val2 is None:
        return (None, False)
    diff = abs(val1 - val2)
    equal = diff < 0.0001
    return (val1, equal)
if __name__ == '__main__':
    sample_d1 = "5"
    sample_d2 = "3.7"
    result_val, is_equal = compare_distances(sample_d1, sample_d2)
    if not is_equal:
        print(f"Difference detected between {sample_d1} and {sample_d2}")
    else:
        print("Distances are equal")
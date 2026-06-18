import re
def validate_distance_string(s: str) -> float | None:
    pattern = r'^-?\d+(\.\d+)?$'
    if not isinstance(s, str):
        return None
    match = re.match(pattern, s.strip())
    if not match:
        return None
    try:
        return float(match.group(0))
    except ValueError:
        return None
def compare_distances(d1_str: str | int | float, d2_str: str | int | float) -> tuple[bool, list[str]]:
    errors = []
    def convert_and_validate(val):
        if isinstance(val, (int, float)):
            val_str = f"{val}"
        else:
            val_str = str(val)
        result = validate_distance_string(val_str)
        if result is None:
            return False, [f"Invalid distance format for {val}"]
        return True, []
    valid1, err1 = convert_and_validate(d1_str)
    errors.extend(err1)
    valid2, err2 = convert_and_validate(d2_str)
    errors.extend(err2)
    if not (valid1 and valid2):
        return False, errors
    d1_val: float = validate_distance_string(str(d1_str)) or 0.0
    d2_val: float = validate_distance_string(str(d2_str)) or 0.0
    diff = abs(d1_val - d2_val)
    is_equal = (diff < 1e-9)
    return is_equal, errors
if __name__ == '__main__':
    sample_d1 = "5.5"
    sample_d2 = "3.0"
    result, messages = compare_distances(sample_d1, sample_d2)
    print(f"Difference: {abs(float(sample_d1) - float(sample_d2))}")
    if not result:
        for msg in messages:
            print(msg)
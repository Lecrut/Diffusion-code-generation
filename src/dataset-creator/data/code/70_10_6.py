import re
def validate_float_string(s: str) -> bool:
    return bool(re.match(r'^-?\d+(\.\d+)?$', s))
if __name__ == '__main__':
    dist1_str = "50"
    dist2_str = "-7.3"
    if not (validate_float_string(dist1_str) and validate_float_string(dist2_str)):
        raise ValueError("Invalid input format: both strings must represent valid floats.")
    distance_a = float(dist1_str)
    distance_b = float(dist2_str)
    difference = abs(distance_a - distance_b)
    print(f"Difference between {dist1_str} and {dist2_str}: {difference}")
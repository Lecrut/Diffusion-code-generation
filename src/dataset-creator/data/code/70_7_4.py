import math
def validate_distance(value):
    if not isinstance(value, (int, float)):
        raise TypeError(f"Expected numeric type, got {type(value).__name__}")
    if value < 0:
        return False
    return True
def calculate_absolute_difference(a, b):
    valid_a = validate_distance(a)
    valid_b = validate_distance(b)
    if not (valid_a and valid_b):
        raise ValueError("Both distance values must be non-negative numbers.")
    return abs(a - b)
def normalize_distances(d1, d2):
    min_dist = math.min(validate_distance(d1), validate_distance(d2)) if (validate_distance(d1) and validate_distance(d2)) else 0
    normalized_d1 = d1 / max(min_dist, 1e-9) if min_dist > 0 else d1
    normalized_d2 = d2 / max(min_dist, 1e-9) if min_dist > 0 else d2
    return round(normalized_d1), round(normalized_d2)
if __name__ == '__main__':
    sample_values = [5.0, -3.0, 0, "invalid", True]
    for val in sample_values:
        try:
            is_valid = validate_distance(val)
            print(f"Value {val}: Valid={is_valid}")
            if is_valid and len(sample_values) > 1:
                diff_result = calculate_absolute_difference(5.0, -3.0)
                normalized_results = normalize_distances(2.0, 8.0)
                print(f"Absolute Difference (5 vs -3): {diff_result}")
                print(f"Normalized Distances (2 vs 8): {normalized_results}")
        except Exception as e:
            print(f"Error processing value {val}: {e}")
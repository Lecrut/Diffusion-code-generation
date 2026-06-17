def calculate_scaled_ratio(ratio_a, ratio_b, target):
    if ratio_a == 0:
        if target == 0:
            return 0.0
        else:
            raise ValueError("Cannot scale ratio when the first term is zero and target is non-zero.")
    scale_factor = target / ratio_a
    new_ratio_a = ratio_a * scale_factor
    new_ratio_b = ratio_b * scale_factor
    return new_ratio_a, new_ratio_b
if __name__ == '__main__':
    ratio1 = 2
    ratio2 = 3
    target_value = 10
    try:
        result_a, result_b = calculate_scaled_ratio(ratio1, ratio2, target_value)
        print(f"Original Ratio: {ratio1}:{ratio2}")
        print(f"Target Value (First Term): {target_value}")
        print(f"New Scaled Ratio: {result_a}:{result_b}")
    except ValueError as e:
        print(f"Error: {e}")
    ratio3 = 4
    ratio4 = 6
    target_value2 = 12
    try:
        result_a2, result_b2 = calculate_scaled_ratio(ratio3, ratio4, target_value2)
        print(f"\nOriginal Ratio: {ratio3}:{ratio4}")
        print(f"Target Value (First Term): {target_value2}")
        print(f"New Scaled Ratio: {result_a2}:{result_b2}")
    except ValueError as e:
        print(f"Error: {e}")
def calculate_scaled_ratio(ratio_a, ratio_b, target):
    if target == 0:
        return None
    scale_factor = target / ratio_a
    new_ratio_a = ratio_a * scale_factor
    new_ratio_b = ratio_b * scale_factor
    return (new_ratio_a, new_ratio_b)
if __name__ == '__main__':
    ratio1 = 2
    ratio2 = 3
    target_value = 10
    result = calculate_scaled_ratio(ratio1, ratio2, target_value)
    print(result)
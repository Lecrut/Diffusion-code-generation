def calculate_scaled_ratio(ratio_num, ratio_den, target):
    if ratio_den == 0:
        raise ValueError("Denominator of the ratio cannot be zero")
    scale_factor = target / ratio_num
    new_ratio_num = ratio_num * scale_factor
    new_ratio_den = ratio_den * scale_factor
    return new_ratio_num, new_ratio_den
if __name__ == '__main__':
    ratio_num_sample = 2
    ratio_den_sample = 3
    target_value_sample = 10
    try:
        result_num, result_den = calculate_scaled_ratio(ratio_num_sample, ratio_den_sample, target_value_sample)
        print(f"Original Ratio: {ratio_num_sample}/{ratio_den_sample}")
        print(f"Target Value (First Term): {target_value_sample}")
        print(f"New Scaled Ratio: {result_num}/{result_den}")
    except ValueError as e:
        print(f"Error: {e}")
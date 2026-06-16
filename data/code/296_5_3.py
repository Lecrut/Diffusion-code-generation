def calculate_scaled_ratio(ratio1, ratio2, target):
    if target == 0:
        return None
    original_sum = ratio1 + ratio2
    if original_sum == 0:
        return None
    scale_factor = target / ratio1
    new_ratio1 = ratio1 * scale_factor
    new_ratio2 = ratio2 * scale_factor
    return (new_ratio1, new_ratio2)
if __name__ == '__main__':
    r1 = 2
    r2 = 3
    t = 10
    result = calculate_scaled_ratio(r1, r2, t)
    print(result)
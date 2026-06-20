def get_larger_in_original_unit(val1_meters, val2_meters):
    val1_cm = val1_meters * 100
    val2_cm = val2_meters * 100
    if val1_cm > val2_cm:
        return val1_meters
    return val2_meters

if __name__ == '__main__':
    sample_a = 1.5
    sample_b = 2.3
    result = get_larger_in_original_unit(sample_a, sample_b)
    print(result)
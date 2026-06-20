def get_larger_value_meters(val1_m, val2_m):
    val1_cm = val1_m * 100
    val2_cm = val2_m * 100
    if val1_cm > val2_cm:
        return val1_m
    return val2_m

if __name__ == '__main__':
    sample_val1 = 1.5
    sample_val2 = 1.4
    result = get_larger_value_meters(sample_val1, sample_val2)
    print(result)
def get_larger_value_in_original_unit(value_m1, value_m2):
    cm1 = value_m1 * 100
    cm2 = value_m2 * 100
    if cm1 > cm2:
        return value_m1
    else:
        return value_m2

if __name__ == '__main__':
    val1 = 1.5
    val2 = 2.0
    result = get_larger_value_in_original_unit(val1, val2)
    print(result)
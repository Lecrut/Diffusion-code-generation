def get_larger_in_original_unit(meters_a, meters_b):
    cm_a = meters_a * 100
    cm_b = meters_b * 100
    if cm_a > cm_b:
        return meters_a
    else:
        return meters_b

if __name__ == '__main__':
    val1 = 5.5
    val2 = 4.2
    result = get_larger_in_original_unit(val1, val2)
    print(result)
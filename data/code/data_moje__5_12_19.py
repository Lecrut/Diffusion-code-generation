def compare_and_return_larger_in_original_units(value1_meters, value2_meters):
    value1_cm = value1_meters * 100
    value2_cm = value2_meters * 100
    if value1_cm > value2_cm:
        return value1_meters
    else:
        return value2_meters

if __name__ == '__main__':
    result = compare_and_return_larger_in_original_units(1.5, 2.0)
    print(result)
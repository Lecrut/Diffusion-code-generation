def adjust_distance(value, unit):
    if unit == 'miles':
        return value * 1.609344
    elif unit == 'km':
        return value / 1.609344
    else:
        raise ValueError("Unit must be 'miles' or 'km'")

if __name__ == '__main__':
    sample_value = 10
    sample_unit = 'miles'
    result = adjust_distance(sample_value, sample_unit)
    print(result)
    sample_value_2 = 100
    sample_unit_2 = 'km'
    result_2 = adjust_distance(sample_value_2, sample_unit_2)
    print(result_2)
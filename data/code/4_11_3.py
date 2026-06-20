def adjust_distance(value, unit):
    if unit == 'miles':
        factor = 1.60934
        return value * factor
    elif unit == 'km':
        factor = 0.621371
        return value * factor
    else:
        raise ValueError("Unsupported unit type")

if __name__ == '__main__':
    sample_value = 10
    sample_unit = 'miles'
    result = adjust_distance(sample_value, sample_unit)
    print(result)
    result_kg = adjust_distance(result, 'km')
    print(result_kg)
def convert_distance(value, unit, conversion_factor):
    if unit == 'miles':
        return value * conversion_factor
    elif unit == 'kilometers':
        return value / conversion_factor
    else:
        raise ValueError("Unit must be 'miles' or 'kilometers'")

if __name__ == '__main__':
    sample_value = 10
    sample_unit = 'miles'
    sample_factor = 1.60934
    result = convert_distance(sample_value, sample_unit, sample_factor)
    print(result)
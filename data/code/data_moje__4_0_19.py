def convert_distance(value, from_unit, to_unit):
    valid_units = {'meters', 'kilometers', 'miles'}
    if from_unit not in valid_units or to_unit not in valid_units:
        raise ValueError("Invalid unit. Use 'meters', 'kilometers', or 'miles'.")
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number.")
    if value < 0:
        raise ValueError("Distance cannot be negative.")
    if from_unit == to_unit:
        return value
    if from_unit == 'meters':
        if to_unit == 'kilometers':
            return value / 1000.0
        elif to_unit == 'miles':
            return value / 1609.344
    elif from_unit == 'kilometers':
        if to_unit == 'meters':
            return value * 1000.0
        elif to_unit == 'miles':
            return value / 1.609344
    elif from_unit == 'miles':
        if to_unit == 'meters':
            return value * 1609.344
        elif to_unit == 'kilometers':
            return value * 1.609344
    raise RuntimeError("Conversion logic error.")

if __name__ == '__main__':
    result1 = convert_distance(1000, 'meters', 'kilometers')
    print(result1)
    result2 = convert_distance(1, 'kilometers', 'miles')
    print(result2)
    result3 = convert_distance(1, 'miles', 'meters')
    print(result3)
    result4 = convert_distance(5280, 'meters', 'miles')
    print(result4)
    result5 = convert_distance(0, 'meters', 'kilometers')
    print(result5)
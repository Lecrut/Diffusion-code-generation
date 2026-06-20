def convert_distance(value, from_unit, to_unit):
    if value < 0:
        raise ValueError("Distance cannot be negative")
    valid_units = {'meters', 'kilometers', 'miles'}
    if from_unit not in valid_units or to_unit not in valid_units:
        raise ValueError("Invalid unit specified")
    conversions_to_meters = {
        'meters': 1.0,
        'kilometers': 1000.0,
        'miles': 1609.34
    }
    value_in_meters = value * conversions_to_meters[from_unit]
    result = value_in_meters / conversions_to_meters[to_unit]
    return result

if __name__ == '__main__':
    print(convert_distance(1, 'kilometers', 'meters'))
    print(convert_distance(1, 'miles', 'kilometers'))
    print(convert_distance(1000, 'meters', 'miles'))
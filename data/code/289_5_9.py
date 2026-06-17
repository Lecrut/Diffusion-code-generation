def convert_distance(value, from_unit, to_unit):
    conversions = {
        'km': 1000.0,
        'mi': 1609.34,
        'm': 1.0,
        'ft': 0.3048
    }
    if from_unit == to_unit:
        return value
    if from_unit not in conversions or to_unit not in conversions:
        raise ValueError("Invalid unit specified")
    base_value = value * conversions[from_unit] / conversions[to_unit]
    return base_value
if __name__ == '__main__':
    print(convert_distance(10, 'km', 'mi'))
    print(convert_distance(10, 'mi', 'km'))
    print(convert_distance(500, 'm', 'ft'))
    print(convert_distance(10, 'ft', 'm'))
    print(convert_distance(10, 'km', 'km'))
def convert_length(value, from_unit, to_unit):
    conversions = {
        'm': 1,
        'ft': 0.3048,
        'mi': 1609.34
    }
    if from_unit == to_unit:
        return value
    if from_unit not in conversions or to_unit not in conversions:
        raise ValueError("Invalid unit provided")
    meters = value
    if from_unit != 'm':
        if from_unit == 'ft':
            meters = value * conversions['ft']
        elif from_unit == 'mi':
            meters = value * conversions['mi']
        else:
            raise ValueError("Unsupported 'from' unit")
    if to_unit != 'm':
        if to_unit == 'ft':
            return meters / conversions['ft']
        elif to_unit == 'mi':
            return meters / conversions['mi']
        else:
            raise ValueError("Unsupported 'to' unit")
    return meters
if __name__ == '__main__':
    print(convert_length(10, 'm', 'ft'))
    print(convert_length(607.2, 'ft', 'm'))
    print(convert_length(1, 'mi', 'm'))
    print(convert_length(5, 'm', 'mi'))
    print(convert_length(10, 'ft', 'mi'))
    try:
        convert_length(10, 'm', 'km')
    except ValueError as e:
        print(f"Error caught: {e}")
def convert_length(value, from_unit, to_unit):
    conversions = {
        'm': 1,
        'ft': 0.3048,
        'mi': 1 / 1609.34
    }
    if from_unit == to_unit:
        return value
    if from_unit not in conversions or to_unit not in conversions:
        raise ValueError("Invalid unit specified")
    meters = value * conversions.get(from_unit, 1)
    result = meters
    if to_unit == 'm':
        return result
    if to_unit == 'ft':
        return result / conversions['ft']
    if to_unit == 'mi':
        return result / conversions['mi']
    raise ValueError("Conversion not supported between these units")
if __name__ == '__main__':
    print(convert_length(10, 'm', 'ft'))
    print(convert_length(66, 'ft', 'm'))
    print(convert_length(1, 'mi', 'm'))
    print(convert_length(100, 'm', 'mi'))
    print(convert_length(5, 'ft', 'mi'))
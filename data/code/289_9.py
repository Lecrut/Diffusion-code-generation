def convert_distance(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'm' and to_unit == 'cm':
        return value * 100
    elif from_unit == 'cm' and to_unit == 'm':
        return value / 100
    elif from_unit == 'km' and to_unit == 'm':
        return value * 1000
    elif from_unit == 'm' and to_unit == 'km':
        return value / 1000
    else:
        raise ValueError("Unsupported unit conversion")
if __name__ == '__main__':
    value = 15.5
    from_unit = 'm'
    to_unit = 'cm'
    result = convert_distance(value, from_unit, to_unit)
    print(result)
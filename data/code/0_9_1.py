import math
def convert_length(value, from_unit, to_unit):
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
    elif from_unit == 'mi' and to_unit == 'km':
        return value * 1.609344
    elif from_unit == 'km' and to_unit == 'mi':
        return value / 1.609344
    elif from_unit == 'in' and to_unit == 'cm':
        return value * 2.54
    elif from_unit == 'cm' and to_unit == 'in':
        return value / 2.54
    else:
        raise ValueError("Unsupported unit conversion")
if __name__ == '__main__':
    length = 10
    from_unit = 'm'
    to_unit = 'km'
    result = convert_length(length, from_unit, to_unit)
    print(f"{length} {from_unit} is equal to {result} {to_unit}")
    length = 100
    from_unit = 'in'
    to_unit = 'cm'
    result = convert_length(length, from_unit, to_unit)
    print(f"{length} {from_unit} is equal to {result} {to_unit}")
    length = 5
    from_unit = 'km'
    to_unit = 'mi'
    result = convert_length(length, from_unit, to_unit)
    print(f"{length} {from_unit} is equal to {result} {to_unit}")
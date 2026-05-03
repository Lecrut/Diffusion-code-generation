import math
def convert_length(length, from_unit, to_unit):
    if from_unit == to_unit:
        return length
    if from_unit == 'm' and to_unit == 'cm':
        return length * 100
    elif from_unit == 'cm' and to_unit == 'm':
        return length / 100
    elif from_unit == 'km' and to_unit == 'm':
        return length * 1000
    elif from_unit == 'm' and to_unit == 'km':
        return length / 1000
    elif from_unit == 'm' and to_unit == 'in':
        return length * 39.3701
    elif from_unit == 'in' and to_unit == 'm':
        return length / 39.3701
    elif from_unit == 'ft' and to_unit == 'm':
        return length * 0.3048
    elif from_unit == 'm' and to_unit == 'ft':
        return length / 0.3048
    else:
        raise ValueError("Unsupported unit conversion")
if __name__ == '__main__':
    length_value = 10
    from_unit_val = 'm'
    to_unit_val = 'km'
    result = convert_length(length_value, from_unit_val, to_unit_val)
    print(f"{length_value} {from_unit_val} is equal to {result} {to_unit_val}")
    length_value = 100
    from_unit_val = 'cm'
    to_unit_val = 'm'
    result = convert_length(length_value, from_unit_val, to_unit_val)
    print(f"{length_value} {from_unit_val} is equal to {result} {to_unit_val}")
    length_value = 10
    from_unit_val = 'm'
    to_unit_val = 'in'
    result = convert_length(length_value, from_unit_val, to_unit_val)
    print(f"{length_value} {from_unit_val} is equal to {result} {to_unit_val}")
    length_value = 10
    from_unit_val = 'ft'
    to_unit_val = 'm'
    result = convert_length(length_value, from_unit_val, to_unit_val)
    print(f"{length_value} {from_unit_val} is equal to {result} {to_unit_val}")
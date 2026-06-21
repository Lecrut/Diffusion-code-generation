M_TO_CM = 100
CM_TO_M = 0.01
M_TO_IN = 39.3701
IN_TO_M = 0.0254
CM_TO_IN = 0.393701
IN_TO_CM = 2.54

def convert_length(value, from_unit, to_unit):
    if from_unit == 'm' and to_unit == 'cm':
        return value * M_TO_CM
    elif from_unit == 'cm' and to_unit == 'm':
        return value * CM_TO_M
    elif from_unit == 'm' and to_unit == 'in':
        return value * M_TO_IN
    elif from_unit == 'in' and to_unit == 'm':
        return value * IN_TO_M
    elif from_unit == 'cm' and to_unit == 'in':
        return value * CM_TO_IN
    elif from_unit == 'in' and to_unit == 'cm':
        return value * IN_TO_CM
    else:
        raise ValueError("Unsupported unit conversion")

if __name__ == '__main__':
    sample_values = [
        (1, 'm', 'cm'),
        (2.54, 'cm', 'in'),
        (10, 'in', 'm')
    ]
    for value, from_unit, to_unit in sample_values:
        converted_value = convert_length(value, from_unit, to_unit)
        print(f"{value} {from_unit} is {converted_value} {to_unit}")
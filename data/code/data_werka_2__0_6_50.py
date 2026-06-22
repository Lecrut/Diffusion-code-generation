def convert_length(value, unit):
    if unit == 'm':
        return value * 3.28084
    elif unit == 'ft':
        return value / 3.28084
    else:
        raise ValueError('Unsupported unit type')
if __name__ == '__main__':
    length_meters = 15.5
    try:
        converted_length_feet = convert_length(length_meters, 'm')
        print(f'{length_meters} meters is {converted_length_feet:.4f} feet')
    except ValueError as e:
        print(e)
    length_feet = 50.5
    try:
        converted_length_meters = convert_length(length_feet, 'ft')
        print(f'{length_feet} feet is {converted_length_meters:.4f} meters')
    except ValueError as e:
        print(e)
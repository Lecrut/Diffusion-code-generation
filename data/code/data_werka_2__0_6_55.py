def convert_length(value, unit):
    if unit == 'm':
        return value * 3.28084
    elif unit == 'ft':
        return value / 3.28084
    else:
        raise ValueError('Unsupported unit type')
if __name__ == '__main__':
    length_meters = 10
    length_feet = 30
    converted_to_feet = convert_length(length_meters, 'm')
    converted_to_meters = convert_length(length_feet, 'ft')
    print(f'{length_meters} meters is {converted_to_feet} feet')
    print(f'{length_feet} feet is {converted_to_meters} meters')
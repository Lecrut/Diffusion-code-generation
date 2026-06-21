def convert_length(value, unit):
    if unit == 'm':
        return value * 3.28084
    elif unit == 'ft':
        return value / 3.28084
    else:
        raise ValueError('Unsupported unit type')
if __name__ == '__main__':
    length_in_meters = 10
    converted_length_feet = convert_length(length_in_meters, 'm')
    print(f'{length_in_meters} meters is {converted_length_feet} feet')
    length_in_feet = 32.8084
    converted_length_meters = convert_length(length_in_feet, 'ft')
    print(f'{length_in_feet} feet is {converted_length_meters} meters')
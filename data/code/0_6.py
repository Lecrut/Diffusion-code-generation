def convert_length(value, unit):
    if unit == 'm':
        return value * 3.28084
    elif unit == 'ft':
        return value / 3.28084
    else:
        raise ValueError('Unsupported unit type')
if __name__ == '__main__':
    length_in_meters = 10
    length_in_feet = convert_length(length_in_meters, 'm')
    print(f'{length_in_meters} meters is {length_in_feet} feet')
    length_in_feet = 32.8084
    length_in_meters = convert_length(length_in_feet, 'ft')
    print(f'{length_in_feet} feet is {length_in_meters} meters')
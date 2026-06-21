def convert_length(value, unit):
    if unit == 'm':
        return value * 3.28084
    elif unit == 'ft':
        return value / 3.28084
    else:
        raise ValueError('Unsupported unit type')
if __name__ == '__main__':
    length_meters = 10
    length_feet = convert_length(length_meters, 'm')
    print(f'{length_meters} meters is {length_feet} feet')
    length_feet = 32.8084
    length_meters = convert_length(length_feet, 'ft')
    print(f'{length_feet} feet is {length_meters} meters')
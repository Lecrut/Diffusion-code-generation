def convert_length(value, unit):
    if unit == 'm':
        return value * 3.28084
    elif unit == 'ft':
        return value / 3.28084
    else:
        raise ValueError('Unsupported unit type')

if __name__ == '__main__':
    length_in_meters = 5
    length_in_feet = convert_length(length_in_meters, 'm')
    print(f'{length_in_meters} meters is {length_in_feet:.2f} feet')
    
    length_in_feet = 16.4042
    length_in_meters = convert_length(length_in_feet, 'ft')
    print(f'{length_in_feet} feet is {length_in_meters:.2f} meters')
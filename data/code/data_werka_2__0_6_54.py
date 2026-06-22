def convert_length(value, unit):
    if unit == 'm':
        conversion_factor = 3.28084
        return value * conversion_factor
    elif unit == 'ft':
        conversion_factor = 1 / 3.28084
        return value * conversion_factor
    else:
        raise ValueError('Unsupported unit type')

if __name__ == '__main__':
    length_meters = 5
    try:
        length_feet = convert_length(length_meters, 'm')
        print(f'{length_meters} meters is {length_feet:.4f} feet')
    except ValueError as e:
        print(e)
    
    length_feet = 16.4042
    try:
        length_meters = convert_length(length_feet, 'ft')
        print(f'{length_feet} feet is {length_meters:.4f} meters')
    except ValueError as e:
        print(e)
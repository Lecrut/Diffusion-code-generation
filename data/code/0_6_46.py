def convert_length(value, unit):
    conversion_factors = {
        'm': 3.28084,
        'ft': 1 / 3.28084
    }
    
    if unit not in conversion_factors:
        raise ValueError('Unsupported unit type')
    
    factor = conversion_factors[unit]
    converted_value = value * factor
    return converted_value

if __name__ == '__main__':
    length_in_meters = 15
    try:
        length_in_feet = convert_length(length_in_meters, 'm')
        print(f'{length_in_meters} meters is {length_in_feet:.4f} feet')
    except ValueError as e:
        print(e)
    
    length_in_feet = 50
    try:
        length_in_meters = convert_length(length_in_feet, 'ft')
        print(f'{length_in_feet} feet is {length_in_meters:.4f} meters')
    except ValueError as e:
        print(e)
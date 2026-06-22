CONVERSION_FACTOR_M_TO_FT = 3.28084

def convert_length(value, unit):
    if unit == 'm':
        return value * CONVERSION_FACTOR_M_TO_FT
    elif unit == 'ft':
        return value / CONVERSION_FACTOR_M_TO_FT
    else:
        raise ValueError('Unsupported unit type')

if __name__ == '__main__':
    sample_length_meters = 12.0
    converted_feet = convert_length(sample_length_meters, 'm')
    print(f'{sample_length_meters} meters is {converted_feet:.4f} feet')
    
    sample_length_feet = 40.0
    converted_meters = convert_length(sample_length_feet, 'ft')
    print(f'{sample_length_feet} feet is {converted_meters:.4f} meters')
METERS_TO_FEET = 3.28084
FEET_TO_METERS = 1 / METERS_TO_FEET

def convert_length(value, unit):
    if unit == 'm':
        return value * METERS_TO_FEET
    elif unit == 'ft':
        return value * FEET_TO_METERS
    else:
        raise ValueError('Unsupported unit type')

if __name__ == '__main__':
    length_in_meters = 20
    converted_length_ft = convert_length(length_in_meters, 'm')
    print(f'{length_in_meters} meters is {converted_length_ft:.4f} feet')
    
    length_in_feet = 65.6168
    converted_length_m = convert_length(length_in_feet, 'ft')
    print(f'{length_in_feet} feet is {converted_length_m:.4f} meters')
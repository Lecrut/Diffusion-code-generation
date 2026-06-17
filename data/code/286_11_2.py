def convert_length(length, unit):
    if unit == 'm':
        return length
    elif unit == 'ft':
        return length * 3.28084
    else:
        raise ValueError("Invalid unit type. Must be 'm' or 'ft'.")
if __name__ == '__main__':
    length_meters = 10.0
    unit_meters = 'm'
    converted_meters = convert_length(length_meters, unit_meters)
    print(f"Input: {length_meters} {unit_meters}, Output: {converted_meters}")
    length_feet = 10.0
    unit_feet = 'ft'
    converted_feet = convert_length(length_feet, unit_feet)
    print(f"Input: {length_feet} {unit_feet}, Output: {converted_feet}")
    length_float = 5.5
    unit_meters_float = 'm'
    converted_meters_float = convert_length(length_float, unit_meters_float)
    print(f"Input: {length_float} {unit_meters_float}, Output: {converted_meters_float}")
    length_float_ft = 5.5
    unit_feet_float = 'ft'
    converted_feet_float = convert_length(length_float_ft, unit_feet_float)
    print(f"Input: {length_float_ft} {unit_feet_float}, Output: {converted_feet_float}")
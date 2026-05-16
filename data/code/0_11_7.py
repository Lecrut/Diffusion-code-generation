def convert_length(length, unit):
    if unit == 'm':
        return length
    elif unit == 'ft':
        return length * 3.28084
    else:
        raise ValueError("Invalid unit type. Must be 'm' or 'ft'.")
if __name__ == '__main__':
    length_meters = 10
    unit_meters = 'm'
    converted_meters = convert_length(length_meters, unit_meters)
    print(f"Converted value: {converted_meters}")
    length_feet = 10
    unit_feet = 'ft'
    converted_feet = convert_length(length_feet, unit_feet)
    print(f"Converted value: {converted_feet}")
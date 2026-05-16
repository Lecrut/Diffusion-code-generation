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
    print(f"10 {unit_meters} is {converted_meters} meters")
    length_feet = 10
    unit_feet = 'ft'
    converted_feet = convert_length(length_feet, unit_feet)
    print(f"10 {unit_feet} is {converted_feet} feet")
    length_meters_2 = 5
    unit_meters_2 = 'm'
    converted_meters_2 = convert_length(length_meters_2, unit_meters_2)
    print(f"5 {unit_meters_2} is {converted_meters_2} meters")
    length_feet_2 = 5
    unit_feet_2 = 'ft'
    converted_feet_2 = convert_length(length_feet_2, unit_feet_2)
    print(f"5 {unit_feet_2} is {converted_feet_2} feet")
import math
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
    result_meters = convert_length(length_meters, unit_meters)
    print(f"10 {unit_meters} is {result_meters:.4f} in meters")
    length_feet = 10
    unit_feet = 'ft'
    result_feet = convert_length(length_feet, unit_feet)
    print(f"10 {unit_feet} is {result_feet:.4f} in feet")
    length_meters_2 = 5
    unit_meters_2 = 'm'
    result_meters_2 = convert_length(length_meters_2, unit_meters_2)
    print(f"5 {unit_meters_2} is {result_meters_2:.4f} in meters")
    length_feet_2 = 5
    unit_feet_2 = 'ft'
    result_feet_2 = convert_length(length_feet_2, unit_feet_2)
    print(f"5 {unit_feet_2} is {result_feet_2:.4f} in feet")
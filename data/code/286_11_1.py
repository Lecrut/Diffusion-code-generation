def convert_length(length, unit):
    if unit == 'm':
        return length
    elif unit == 'ft':
        return length * 3.28084
    else:
        raise ValueError("Invalid unit specified. Use 'm' or 'ft'.")
if __name__ == '__main__':
    length_meters = 10.0
    unit_meters = 'm'
    converted_meters = convert_length(length_meters, unit_meters)
    print(f"{length_meters} {unit_meters} is {converted_meters}")
    length_feet = 10.0
    unit_feet = 'ft'
    converted_feet = convert_length(length_feet, unit_feet)
    print(f"{length_feet} {unit_feet} is {converted_feet}")
    length_float = 5.5
    unit_meters_2 = 'm'
    converted_meters_2 = convert_length(length_float, unit_meters_2)
    print(f"{length_float} {unit_meters_2} is {converted_meters_2}")
    length_float_ft = 5.5
    unit_feet_2 = 'ft'
    converted_feet_2 = convert_length(length_float_ft, unit_feet_2)
    print(f"{length_float_ft} {unit_feet_2} is {converted_feet_2}")
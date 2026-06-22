conversion_factors = {
    'm': 1.0,
    'ft': 3.28084
}

def convert_length(length, from_unit, to_unit):
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Invalid unit type. Must be 'm' or 'ft'.")
    return length * (conversion_factors[from_unit] / conversion_factors[to_unit])

if __name__ == '__main__':
    length_feet = 10.0
    from_unit_feet = 'ft'
    to_unit_meters = 'm'
    result_meters = convert_length(length_feet, from_unit_feet, to_unit_meters)
    print(f"10.0 ft converted to meters: {result_meters}")
    
    length_feet_2 = 5.5
    from_unit_feet_2 = 'ft'
    to_unit_meters_2 = 'm'
    result_meters_2 = convert_length(length_feet_2, from_unit_feet_2, to_unit_meters_2)
    print(f"5.5 ft converted to meters: {result_meters_2}")
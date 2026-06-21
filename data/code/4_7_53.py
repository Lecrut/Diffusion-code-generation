def validate_units(from_unit, to_unit):
    supported_conversions = {
        ('miles', 'kilometers'),
        ('kilometers', 'miles')
    }
    if (from_unit, to_unit) not in supported_conversions:
        raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}")

def convert_distance(distance, from_unit, to_unit):
    validate_units(from_unit, to_unit)
    
    conversion_factors = {
        ('miles', 'kilometers'): 1.60934,
        ('kilometers', 'miles'): 0.621371,
    }
    return distance * conversion_factors[(from_unit, to_unit)]

if __name__ == '__main__':
    sample_distance_miles = 8
    sample_distance_kilometers = 13
    converted_to_km = convert_distance(sample_distance_miles, 'miles', 'kilometers')
    converted_to_miles = convert_distance(sample_distance_kilometers, 'kilometers', 'miles')
    print(f"{sample_distance_miles} miles is {converted_to_km:.2f} kilometers")
    print(f"{sample_distance_kilometers} kilometers is {converted_to_miles:.2f} miles")
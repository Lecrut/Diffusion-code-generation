def convert_distance(distance, from_unit, to_unit):
    conversion_factors = {
        ('miles', 'kilometers'): 1.60934,
        ('kilometers', 'miles'): 0.621371,
    }
    
    if (from_unit, to_unit) not in conversion_factors:
        raise ValueError("Invalid unit conversion")
    
    return distance * conversion_factors[(from_unit, to_unit)]

if __name__ == '__main__':
    sample_distance_miles = 5
    sample_distance_kilometers = 10
    
    converted_to_km = convert_distance(sample_distance_miles, 'miles', 'kilometers')
    converted_to_miles = convert_distance(sample_distance_kilometers, 'kilometers', 'miles')
    
    print(f"{sample_distance_miles} miles is {converted_to_km:.2f} kilometers")
    print(f"{sample_distance_kilometers} kilometers is {converted_to_miles:.2f} miles")
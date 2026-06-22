def convert_distance(distance, from_unit, to_unit):
    conversion_factors = {
        'miles_to_kilometers': 1.60934,
        'kilometers_to_miles': 0.621371,
    }
    
    if from_unit == 'miles' and to_unit == 'kilometers':
        factor_key = 'miles_to_kilometers'
    elif from_unit == 'kilometers' and to_unit == 'miles':
        factor_key = 'kilometers_to_miles'
    else:
        raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}")
    
    return distance * conversion_factors[factor_key]

if __name__ == '__main__':
    sample_distance_miles = 8
    sample_distance_kilometers = 20
    
    converted_to_km = convert_distance(sample_distance_miles, 'miles', 'kilometers')
    converted_to_miles = convert_distance(sample_distance_kilometers, 'kilometers', 'miles')
    
    print(f"{sample_distance_miles} miles is {converted_to_km:.2f} kilometers")
    print(f"{sample_distance_kilometers} kilometers is {converted_to_miles:.2f} miles")
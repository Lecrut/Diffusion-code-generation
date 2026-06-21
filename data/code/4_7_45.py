def convert_distance(distance, from_unit, to_unit):
    MILES_TO_KILOMETERS = 1.60934
    KILOMETERS_TO_MILES = 0.621371
    
    if (from_unit == 'miles' and to_unit == 'kilometers'):
        return distance * MILES_TO_KILOMETERS
    elif (from_unit == 'kilometers' and to_unit == 'miles'):
        return distance * KILOMETERS_TO_MILES
    else:
        raise ValueError("Unsupported unit conversion")

if __name__ == '__main__':
    sample_distance_miles = 8.0
    converted_to_km = convert_distance(sample_distance_miles, 'miles', 'kilometers')
    print(f"{sample_distance_miles} miles is {converted_to_km:.2f} kilometers")
    
    sample_distance_kilometers = 12.874752
    converted_to_miles = convert_distance(sample_distance_kilometers, 'kilometers', 'miles')
    print(f"{sample_distance_kilometers} kilometers is {converted_to_miles:.2f} miles")
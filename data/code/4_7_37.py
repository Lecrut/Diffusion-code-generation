def convert_distance(distance, from_unit, to_unit, conversion_factor):
    if from_unit == 'miles' and to_unit == 'kilometers':
        return distance * conversion_factor
    elif from_unit == 'kilometers' and to_unit == 'miles':
        return distance / conversion_factor
    else:
        raise ValueError("Unsupported unit conversion")

if __name__ == '__main__':
    sample_distance_miles = 10.0
    sample_conversion_factor = 1.60934
    converted_distance_km = convert_distance(sample_distance_miles, 'miles', 'kilometers', sample_conversion_factor)
    print(f"{sample_distance_miles} miles is {converted_distance_km:.2f} kilometers")

    sample_distance_km = 16.0934
    converted_distance_miles = convert_distance(sample_distance_km, 'kilometers', 'miles', sample_conversion_factor)
    print(f"{sample_distance_km} kilometers is {converted_distance_miles:.2f} miles")
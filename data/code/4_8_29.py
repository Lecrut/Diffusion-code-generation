def convert_distance(distance, unit):
    if unit == 'km':
        return distance * 0.621371
    elif unit == 'mi':
        return distance / 0.621371
    else:
        raise ValueError("Invalid unit. Use 'km' for kilometers or 'mi' for miles.")

if __name__ == '__main__':
    sample_distance_km = 10
    sample_unit_km = 'km'
    converted_distance_km_to_mi = convert_distance(sample_distance_km, sample_unit_km)
    
    sample_distance_mi = 5
    sample_unit_mi = 'mi'
    converted_distance_mi_to_km = convert_distance(sample_distance_mi, sample_unit_mi)
    
    print(f"{sample_distance_km} {sample_unit_km} is {converted_distance_km_to_mi:.2f} miles")
    print(f"{sample_distance_mi} {sample_unit_mi} is {converted_distance_mi_to_km:.2f} kilometers")
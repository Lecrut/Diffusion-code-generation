def convert_distance(distance, unit_from, unit_to):
    if unit_from == 'km' and unit_to == 'mi':
        return distance * 0.621371
    elif unit_from == 'mi' and unit_to == 'km':
        return distance / 0.621371
    else:
        raise ValueError("Invalid units. Use 'km' for kilometers and 'mi' for miles.")

if __name__ == '__main__':
    sample_distance = 10
    converted_distance_km_to_mi = convert_distance(sample_distance, 'km', 'mi')
    print(f"{sample_distance} km is {converted_distance_km_to_mi:.2f} mi")
    
    sample_distance = 5
    converted_distance_mi_to_km = convert_distance(sample_distance, 'mi', 'km')
    print(f"{sample_distance} mi is {converted_distance_mi_to_km:.2f} km")
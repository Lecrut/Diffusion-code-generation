def convert_distance(distance, from_unit, to_unit):
    if from_unit == 'km' and to_unit == 'mi':
        return distance * 0.621371
    elif from_unit == 'mi' and to_unit == 'km':
        return distance / 0.621371
    else:
        raise ValueError("Invalid unit conversion")

if __name__ == '__main__':
    sample_distance_km = 10
    sample_distance_mi = 5

    converted_to_miles = convert_distance(sample_distance_km, 'km', 'mi')
    converted_to_kilometers = convert_distance(sample_distance_mi, 'mi', 'km')

    print(f"{sample_distance_km} km is {converted_to_miles:.2f} mi")
    print(f"{sample_distance_mi} mi is {converted_to_kilometers:.2f} km")
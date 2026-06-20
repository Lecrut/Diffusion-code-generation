def convert_distance(distance, from_unit, to_unit):
    if from_unit.lower() == 'km' and to_unit.lower() == 'mi':
        return distance * 0.621371
    elif from_unit.lower() == 'mi' and to_unit.lower() == 'km':
        return distance / 0.621371
    elif from_unit.lower() == to_unit.lower():
        return distance
    else:
        raise ValueError("Unsupported unit conversion. Use 'km' and 'mi'.")

if __name__ == '__main__':
    sample_distance_km = 10
    sample_distance_mi = 10
    result_km_to_mi = convert_distance(sample_distance_km, 'km', 'mi')
    result_mi_to_km = convert_distance(sample_distance_mi, 'mi', 'km')
    print(result_km_to_mi)
    print(result_mi_to_km)
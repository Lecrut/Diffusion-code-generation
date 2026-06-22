def convert_distance(value, from_unit, to_unit):
    if from_unit.lower() == 'km' and to_unit.lower() == 'mi':
        return value * 0.621371
    elif from_unit.lower() == 'mi' and to_unit.lower() == 'km':
        return value * 1.60934
    else:
        raise ValueError("Unsupported unit conversion")

if __name__ == '__main__':
    km_to_mi = convert_distance(10, 'km', 'mi')
    mi_to_km = convert_distance(5, 'mi', 'km')
    print(km_to_mi)
    print(mi_to_km)
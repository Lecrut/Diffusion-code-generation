def convert_distance(distance, source_unit, target_unit):
    conversion_factors = {
        ('km', 'miles'): 0.621371,
        ('miles', 'km'): 1.60934,
        ('km', 'meters'): 1000,
        ('meters', 'km'): 0.001,
        ('miles', 'meters'): 1609.34,
        ('meters', 'miles'): 0.000621371
    }
    if source_unit == target_unit:
        return distance
    key = (source_unit, target_unit)
    if key in conversion_factors:
        factor = conversion_factors[key]
        return distance * factor
    elif source_unit == 'km':
        if target_unit == 'miles':
            return distance * 0.621371
        elif target_unit == 'meters':
            return distance * 1000
    elif source_unit == 'miles':
        if target_unit == 'km':
            return distance * 1.60934
        elif target_unit == 'meters':
            return distance * 1609.34
    elif source_unit == 'meters':
        if target_unit == 'km':
            return distance * 0.001
        elif target_unit == 'miles':
            return distance * 0.000621371
    else:
        raise ValueError("Unsupported unit conversion")
if __name__ == '__main__':
    distance_km = 10
    source = 'km'
    target = 'miles'
    result1 = convert_distance(distance_km, source, target)
    print(f"{distance_km} {source} is equal to {result1:.2f} {target}")
    distance_miles = 5
    source = 'miles'
    target = 'km'
    result2 = convert_distance(distance_miles, source, target)
    print(f"{distance_miles} {source} is equal to {result2:.2f} {target}")
    distance_meters = 5000
    source = 'meters'
    target = 'km'
    result3 = convert_distance(distance_meters, source, target)
    print(f"{distance_meters} {source} is equal to {result3:.2f} {target}")
    distance_meters_to_miles = 10000
    source = 'meters'
    target = 'miles'
    result4 = convert_distance(distance_meters_to_miles, source, target)
    print(f"{distance_meters_to_miles} {source} is equal to {result4:.2f} {target}")
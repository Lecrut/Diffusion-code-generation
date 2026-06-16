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
        if source_unit == 'km' and target_unit == 'miles':
            return distance * factor
        elif source_unit == 'miles' and target_unit == 'km':
            return distance * factor
        elif source_unit == 'km' and target_unit == 'meters':
            return distance * 1000
        elif source_unit == 'meters' and target_unit == 'km':
            return distance * 0.001
        elif source_unit == 'miles' and target_unit == 'meters':
            return distance * 1609.34
        elif source_unit == 'meters' and target_unit == 'miles':
            return distance * 0.000621371
    if source_unit == 'km' and target_unit == 'miles':
        return distance * 0.621371
    elif source_unit == 'miles' and target_unit == 'km':
        return distance * 1.60934
    elif source_unit == 'km' and target_unit == 'meters':
        return distance * 1000
    elif source_unit == 'meters' and target_unit == 'km':
        return distance * 0.001
    elif source_unit == 'miles' and target_unit == 'meters':
        return distance * 1609.34
    elif source_unit == 'meters' and target_unit == 'miles':
        return distance * 0.000621371
    raise ValueError("Unsupported unit conversion")
if __name__ == '__main__':
    distance_km = 10
    source = 'km'
    target1 = 'miles'
    target2 = 'meters'
    target3 = 'km'
    result1 = convert_distance(distance_km, source, target1)
    print(f"{distance_km} {source} is equal to {result1:.4f} {target1}")
    result2 = convert_distance(distance_km, source, target2)
    print(f"{distance_km} {source} is equal to {result2:.2f} {target2}")
    result3 = convert_distance(distance_km, source, target3)
    print(f"{distance_km} {source} is equal to {result3:.3f} {target3}")
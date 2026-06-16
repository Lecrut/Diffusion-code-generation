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
    if source_unit == 'km' and target_unit == 'meters':
        return distance * 1000
    elif source_unit == 'meters' and target_unit == 'km':
        return distance * 0.001
    raise ValueError("Unsupported unit conversion")
if __name__ == '__main__':
    distance_km = 10
    source = 'km'
    target1 = 'miles'
    target2 = 'meters'
    result1 = convert_distance(distance_km, source, target1)
    print(f"{distance_km} {source} is equal to {result1:.2f} {target1}")
    result2 = convert_distance(distance_km, source, target2)
    print(f"{distance_km} {source} is equal to {result2:.0f} {target2}")
    distance_miles = 5
    source2 = 'miles'
    target3 = 'km'
    result3 = convert_distance(distance_miles, source2, target3)
    print(f"{distance_miles} {source2} is equal to {result3:.2f} {target3}")
    distance_meters = 5000
    source3 = 'meters'
    target4 = 'km'
    result4 = convert_distance(distance_meters, source3, target4)
    print(f"{distance_meters} {source3} is equal to {result4:.2f} {target4}")
    distance_miles2 = 100
    source4 = 'miles'
    target5 = 'meters'
    result5 = convert_distance(distance_miles2, source4, target5)
    print(f"{distance_miles2} {source4} is equal to {result5:.2f} {target5}")
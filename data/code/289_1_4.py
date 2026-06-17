def convert_distance(distance, source_unit, target_unit):
    conversion_factors = {
        ('km', 'miles'): 0.621371,
        ('miles', 'km'): 1.60934,
        ('km', 'meters'): 1000,
        ('meters', 'km'): 0.001,
        ('miles', 'meters'): 1609.34,
        ('meters', 'miles'): 0.000621371,
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
    else:
        if source_unit in ['km', 'miles', 'meters'] and target_unit in ['km', 'miles', 'meters']:
            if source_unit == 'km' and target_unit == 'meters':
                return distance * 1000
            elif source_unit == 'meters' and target_unit == 'km':
                return distance * 0.001
            elif source_unit == 'miles' and target_unit == 'meters':
                return distance * 1609.34
            elif source_unit == 'meters' and target_unit == 'miles':
                return distance * 0.000621371
            elif source_unit == 'km' and target_unit == 'miles':
                return distance * 0.621371
            elif source_unit == 'miles' and target_unit == 'km':
                return distance * 1.60934
    return None
if __name__ == '__main__':
    distance_value = 10
    source = 'km'
    target = 'miles'
    result = convert_distance(distance_value, source, target)
    print(f"{distance_value} {source} is equal to {result:.2f} {target}")
    distance_value = 500
    source = 'meters'
    target = 'km'
    result = convert_distance(distance_value, source, target)
    print(f"{distance_value} {source} is equal to {result:.3f} {target}")
    distance_value = 1
    source = 'miles'
    target = 'meters'
    result = convert_distance(distance_value, source, target)
    print(f"{distance_value} {source} is equal to {result:.2f} {target}")
    distance_value = 10
    source = 'km'
    target = 'km'
    result = convert_distance(distance_value, source, target)
    print(f"{distance_value} {source} is equal to {result:.2f} {target}")
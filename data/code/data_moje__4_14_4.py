def convert_distance(value, source_unit):
    if not isinstance(value, (int, float)):
        raise TypeError('Value must be a number')
    if not isinstance(source_unit, str):
        raise TypeError('Source unit must be a string')
    source_unit = source_unit.lower().strip()
    if source_unit not in ('meters', 'km', 'kilometers', 'miles', 'ft', 'feet'):
        raise ValueError(f'Unsupported unit: {source_unit}')
    if value < 0:
        raise ValueError('Distance cannot be negative')
    if source_unit in ('meters', 'm'):
        meters = float(value)
    elif source_unit in ('km', 'kilometers'):
        meters = float(value) * 1609.344
    elif source_unit in ('miles',):
        meters = float(value) * 1609.344
    elif source_unit in ('ft', 'feet'):
        meters = float(value) * 0.3048
    else:
        meters = float(value)
    return round(meters, 6)

def to_meters(value, source_unit):
    return convert_distance(value, source_unit)

def to_kilometers(value, source_unit):
    meters = convert_distance(value, source_unit)
    return round(meters / 1609.344, 6)

def to_miles(value, source_unit):
    meters = convert_distance(value, source_unit)
    return round(meters / 1609.344, 6)

def to_feet(value, source_unit):
    meters = convert_distance(value, source_unit)
    return round(meters / 0.3048, 6)
if __name__ == '__main__':
    result_meters = convert_distance(1000, 'meters')
    print(result_meters)
    result_kilometers = to_kilometers(1000, 'meters')
    print(result_kilometers)
    result_miles = to_miles(1000, 'meters')
    print(result_miles)
    result_feet = to_feet(1000, 'meters')
    print(result_feet)
    result_miles_from_km = to_miles(5, 'km')
    print(result_miles_from_km)
    result_feet_from_miles = to_feet(1, 'miles')
    print(result_feet_from_miles)
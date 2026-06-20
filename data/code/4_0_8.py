UNIT_TO_METER = {
    'meters': 1.0,
    'kilometers': 1000.0,
    'miles': 1609.34
}

METER_TO_UNIT = {
    'meters': 1.0,
    'kilometers': 0.001,
    'miles': 0.000621371
}

VALID_UNITS = {'meters', 'kilometers', 'miles'}

def convert_distance(value, from_unit, to_unit):
    if value < 0:
        raise ValueError("Distance cannot be negative")
    
    normalized_from = from_unit.lower()
    normalized_to = to_unit.lower()
    
    if normalized_from not in VALID_UNITS:
        raise ValueError(f"Invalid from_unit: {from_unit}")
    if normalized_to not in VALID_UNITS:
        raise ValueError(f"Invalid to_unit: {to_unit}")
    
    value_in_meters = value * UNIT_TO_METER[normalized_from]
    result = value_in_meters * METER_TO_UNIT[normalized_to]
    
    return result

if __name__ == '__main__':
    sample_1 = convert_distance(1000, 'meters', 'kilometers')
    print(sample_1)
    
    sample_2 = convert_distance(1, 'kilometers', 'miles')
    print(sample_2)
    
    sample_3 = convert_distance(5, 'miles', 'meters')
    print(sample_3)
UNIT_CONVERSION_FACTORS = {
    'meters': 1.0,
    'kilometers': 0.001,
    'centimeters': 100.0,
    'millimeters': 1000.0,
    'inches': 39.3701,
    'feet': 3.28084,
    'yards': 1.09361,
    'miles': 0.000621371
}

SUPPORTED_UNITS = set(UNIT_CONVERSION_FACTORS.keys())

def convert_length(value, from_unit, to_unit):
    if from_unit not in SUPPORTED_UNITS:
        raise ValueError(f"Unsupported unit: {from_unit}")
    if to_unit not in SUPPORTED_UNITS:
        raise ValueError(f"Unsupported unit: {to_unit}")
    
    value_in_meters = value / UNIT_CONVERSION_FACTORS[from_unit]
    result = value_in_meters * UNIT_CONVERSION_FACTORS[to_unit]
    return result

if __name__ == '__main__':
    result1 = convert_length(1, 'meters', 'kilometers')
    print(result1)
    
    result2 = convert_length(1, 'miles', 'kilometers')
    print(result2)
    
    result3 = convert_length(100, 'centimeters', 'inches')
    print(result3)
    
    result4 = convert_length(1, 'yards', 'meters')
    print(result4)
    
    result5 = convert_length(50, 'millimeters', 'centimeters')
    print(result5)
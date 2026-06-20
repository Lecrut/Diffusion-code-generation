UNIT_FACTORS = {
    'mm': 0.001,
    'cm': 0.01,
    'm': 1.0,
    'km': 1000.0,
    'in': 0.0254,
    'ft': 0.3048,
    'yd': 0.9144,
    'mi': 1609.344
}

def convert_length(value, from_unit, to_unit):
    if from_unit not in UNIT_FACTORS:
        raise ValueError(f"Unsupported source unit: {from_unit}")
    if to_unit not in UNIT_FACTORS:
        raise ValueError(f"Unsupported target unit: {to_unit}")
    
    value_in_meters = value * UNIT_FACTORS[from_unit]
    result = value_in_meters / UNIT_FACTORS[to_unit]
    return result

if __name__ == '__main__':
    result = convert_length(1, 'km', 'm')
    print(result)
    
    result2 = convert_length(12, 'in', 'cm')
    print(result2)
    
    result3 = convert_length(5280, 'ft', 'mi')
    print(result3)
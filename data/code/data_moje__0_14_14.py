UNIT_CONVERSION_FACTORS = {
    'meter': 1.0,
    'kilometer': 1000.0,
    'centimeter': 0.01,
    'millimeter': 0.001,
    'inch': 0.0254,
    'foot': 0.3048,
    'yard': 0.9144,
    'mile': 1609.344
}

SUPPORTED_UNITS = frozenset(UNIT_CONVERSION_FACTORS.keys())

def convert_length(value, from_unit, to_unit):
    if from_unit not in SUPPORTED_UNITS:
        raise ValueError(f"Unsupported source unit: {from_unit}")
    if to_unit not in SUPPORTED_UNITS:
        raise ValueError(f"Unsupported target unit: {to_unit}")
    
    meters = value * UNIT_CONVERSION_FACTORS[from_unit]
    result = meters / UNIT_CONVERSION_FACTORS[to_unit]
    return result

if __name__ == '__main__':
    sample_length = 100.0
    sample_from = 'meter'
    sample_to = 'foot'
    result = convert_length(sample_length, sample_from, sample_to)
    print(result)
    
    another_length = 1.0
    another_from = 'mile'
    another_to = 'kilometer'
    result2 = convert_length(another_length, another_from, another_to)
    print(result2)
    
    third_length = 5.0
    third_from = 'inch'
    third_to = 'centimeter'
    result3 = convert_length(third_length, third_from, third_to)
    print(result3)
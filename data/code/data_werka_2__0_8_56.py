def convert_length(length, target_unit):
    UNIT_CONVERSIONS = {
        'meters': 1.0,
        'feet': 3.28084,
        'kilometers': 0.001
    }
    
    if target_unit not in UNIT_CONVERSIONS:
        raise ValueError(f"Unsupported unit: {target_unit}")
    
    conversion_factor = UNIT_CONVERSIONS[target_unit]
    return length * conversion_factor

if __name__ == '__main__':
    sample_length = 200
    target_unit = 'meters'
    converted_value = convert_length(sample_length, target_unit)
    print(converted_value)
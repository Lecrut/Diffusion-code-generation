def convert_length(length, target_unit):
    UNIT_CONVERSIONS = {
        'meters': 1.0,
        'feet': 3.28084,
        'kilometers': 0.001
    }
    
    if target_unit not in UNIT_CONVERSIONS:
        raise ValueError(f"Unsupported unit: {target_unit}")
    
    return length * UNIT_CONVERSIONS[target_unit]

if __name__ == '__main__':
    sample_length = 50
    sample_unit = 'kilometers'
    converted_value = convert_length(sample_length, sample_unit)
    print(converted_value)
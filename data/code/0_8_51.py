def convert_length(length, target_unit):
    SUPPORTED_UNITS = {
        'meters': 1.0,
        'feet': 3.28084,
        'kilometers': 0.001
    }
    
    def validate_unit(unit):
        if unit not in SUPPORTED_UNITS:
            raise ValueError(f"Unsupported unit: {unit}")
    
    validate_unit(target_unit)
    conversion_factor = SUPPORTED_UNITS[target_unit]
    return length * conversion_factor

if __name__ == '__main__':
    sample_length = 150
    target_unit = 'meters'
    try:
        converted_value = convert_length(sample_length, target_unit)
        print(converted_value)
    except ValueError as e:
        print(e)
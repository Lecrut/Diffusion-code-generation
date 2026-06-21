def validate_unit(target_unit):
    supported_units = ['meters', 'feet', 'kilometers']
    if target_unit not in supported_units:
        raise ValueError(f"Unsupported unit: {target_unit}")

def convert_length(length, target_unit):
    validate_unit(target_unit)
    
    conversion_factors = {
        'meters': 1.0,
        'feet': 3.28084,
        'kilometers': 0.001
    }
    
    return length * conversion_factors[target_unit]

if __name__ == '__main__':
    sample_length = 75
    target_unit = 'meters'
    converted_value = convert_length(sample_length, target_unit)
    print(converted_value)
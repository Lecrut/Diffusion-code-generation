def convert_length(length, target_unit):
    supported_units = {
        'meters': 1.0,
        'feet': 3.28084,
        'kilometers': 0.001
    }
    
    if target_unit not in supported_units:
        raise ValueError(f"Unsupported unit: {target_unit}")
    
    conversion_factor = supported_units[target_unit]
    converted_value = length * conversion_factor
    
    return converted_value

if __name__ == '__main__':
    sample_length = 200
    sample_unit = 'meters'
    result = convert_length(sample_length, sample_unit)
    print(result)
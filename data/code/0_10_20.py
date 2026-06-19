def convert_length(length, target_unit):
    supported_units = {
        'meters': length,
        'feet': length * 3.28084,
        'kilometers': length / 1000
    }
    
    if target_unit not in supported_units:
        raise ValueError(f"Unsupported unit: {target_unit}")
    
    return supported_units[target_unit]

if __name__ == '__main__':
    sample_length = 100
    sample_unit = 'feet'
    converted_value = convert_length(sample_length, sample_unit)
    print(converted_value)
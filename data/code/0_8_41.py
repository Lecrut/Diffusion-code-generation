def convert_length(length, target_unit):
    supported_units = {
        'meters': 1.0,
        'feet': 3.28084,
        'kilometers': 0.001
    }
    
    if target_unit not in supported_units:
        raise ValueError(f"Unsupported unit: {target_unit}")
    
    return length * supported_units[target_unit]

if __name__ == '__main__':
    sample_length = 100
    target_unit = 'feet'
    converted_length = convert_length(sample_length, target_unit)
    print(converted_length)
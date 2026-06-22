def convert_length(length, target_unit):
    supported_units = {
        'meters': 1.0,
        'feet': 3.28084,
        'kilometers': 0.001
    }
    
    if target_unit not in supported_units:
        raise ValueError(f"Unsupported unit: {target_unit}")
    
    converted_value = length * supported_units[target_unit]
    return converted_value

if __name__ == '__main__':
    sample_length = 100
    sample_unit = 'feet'
    result = convert_length(sample_length, sample_unit)
    print(result)
    
    sample_length_2 = 5
    sample_unit_2 = 'kilometers'
    result_2 = convert_length(sample_length_2, sample_unit_2)
    print(result_2)
    
    sample_length_3 = 0.5
    sample_unit_3 = 'meters'
    result_3 = convert_length(sample_length_3, sample_unit_3)
    print(result_3)
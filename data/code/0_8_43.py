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
    target_units = ['meters', 'feet', 'kilometers', 'inches']
    
    for unit in target_units:
        try:
            converted_length = convert_length(sample_length, unit)
            print(f"{sample_length} meters is {converted_length} {unit}")
        except ValueError as e:
            print(e)
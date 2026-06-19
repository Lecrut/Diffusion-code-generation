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
    target_units = ['meters', 'feet', 'kilometers', 'inches']
    
    for unit in target_units:
        try:
            result = convert_length(sample_length, unit)
            print(f"{sample_length} meters is {result} {unit}")
        except ValueError as e:
            print(e)
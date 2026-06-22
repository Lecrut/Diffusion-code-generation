def convert_length(length, target_unit):
    supported_units = {
        'meters': 1.0,
        'feet': 3.28084,
        'kilometers': 0.001
    }
    
    if target_unit not in supported_units:
        raise ValueError(f"Unsupported unit: {target_unit}")
    
    meters = length / supported_units[target_unit]
    return meters / 1.0

if __name__ == '__main__':
    result = convert_length(100, 'feet')
    print(result)
    
    result2 = convert_length(1, 'kilometers')
    print(result2)
    
    try:
        convert_length(1, 'miles')
    except ValueError as e:
        print(e)
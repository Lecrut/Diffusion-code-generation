def convert_length(length, target_unit):
    supported_units = {
        'meters': 1.0,
        'feet': 3.28084,
        'kilometers': 0.001
    }
    
    if target_unit not in supported_units:
        raise ValueError(f"Unsupported unit: {target_unit}")
    
    length_in_meters = length * supported_units[target_unit]
    result = length_in_meters / supported_units['meters']
    return result

if __name__ == '__main__':
    print(convert_length(100, 'feet'))
    print(convert_length(1, 'kilometers'))
    print(convert_length(5, 'meters'))
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
    length = 100
    target_unit = 'feet'
    converted_length = convert_length(length, target_unit)
    print(converted_length)
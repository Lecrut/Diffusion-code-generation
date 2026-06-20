def convert_length(length, target_unit):
    supported_units = {'meters', 'feet', 'kilometers'}
    if target_unit not in supported_units:
        raise ValueError(f"Unsupported unit: {target_unit}")
    
    conversion_factors = {
        'meters': 1.0,
        'feet': 3.28084,
        'kilometers': 0.001
    }
    
    return length * conversion_factors[target_unit]

if __name__ == '__main__':
    print(convert_length(100, 'meters'))
    print(convert_length(100, 'feet'))
    print(convert_length(100, 'kilometers'))
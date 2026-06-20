def convert_length(length, target_unit):
    supported_units = {'meters': 1, 'feet': 0.3048, 'kilometers': 1000}
    
    if target_unit not in supported_units:
        raise ValueError(f"Unsupported unit: {target_unit}")
    
    meters = length * supported_units[target_unit]
    
    conversion_factors = {
        'meters': 1.0 / supported_units['meters'],
        'feet': 1.0 / supported_units['feet'],
        'kilometers': 1.0 / supported_units['kilometers']
    }
    
    result = meters * conversion_factors[target_unit]
    return result

if __name__ == '__main__':
    print(convert_length(10, 'meters'))
    print(convert_length(10, 'feet'))
    print(convert_length(10, 'kilometers'))
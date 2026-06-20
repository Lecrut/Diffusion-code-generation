def convert_length(length, target_unit):
    SUPPORTED_UNITS = {'meters': 1, 'feet': 3.28084, 'kilometers': 0.001}
    
    if target_unit not in SUPPORTED_UNITS:
        raise ValueError(f"Unsupported unit: {target_unit}")
    
    meters = length / SUPPORTED_UNITS[target_unit]
    
    return meters / SUPPORTED_UNITS['meters']

if __name__ == '__main__':
    result = convert_length(1, 'kilometers')
    print(result)
    
    result2 = convert_length(1000, 'meters')
    print(result2)
    
    result3 = convert_length(1, 'feet')
    print(result3)
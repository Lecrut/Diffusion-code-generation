def convert_length(value, unit):
    conversions = {
        'meters': 1.0,
        'feet': 0.3048,
        'kilometers': 1000.0
    }
    
    if unit not in conversions:
        raise ValueError(f"Unsupported unit: {unit}")
    
    meters = value * conversions[unit]
    
    result_meters = meters
    result_feet = meters / 0.3048
    result_kilometers = meters / 1000.0
    
    if unit == 'meters':
        return result_meters
    elif unit == 'feet':
        return result_feet
    elif unit == 'kilometers':
        return result_kilometers

if __name__ == '__main__':
    print(convert_length(10, 'meters'))
    print(convert_length(10, 'feet'))
    print(convert_length(10, 'kilometers'))
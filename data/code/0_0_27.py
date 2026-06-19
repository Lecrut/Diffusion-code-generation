def convert_length(value: float, unit: str) -> float:
    conversions = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'ft': 0.3048,
        'in': 0.0254,
        'yd': 0.9144,
        'mi': 1609.344,
    }
    
    if unit not in conversions:
        raise ValueError(f"Unsupported unit: {unit}")
    
    meters = value * conversions[unit]
    
    return meters

if __name__ == '__main__':
    result_meters = convert_length(100, 'm')
    print(result_meters)
    
    result_feet = convert_length(1, 'ft')
    print(result_feet)
    
    result_km = convert_length(5, 'km')
    print(result_km)
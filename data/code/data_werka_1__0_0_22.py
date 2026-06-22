def convert_length(value: float, unit: str) -> float:
    conversions = {
        'm': 1.0,
        'ft': 0.3048,
        'cm': 0.01,
        'mm': 0.001,
        'in': 0.0254,
        'km': 1000.0,
        'mi': 1609.344,
    }
    
    if unit not in conversions:
        raise ValueError(f"Unsupported unit: {unit}")
    
    meters = value * conversions[unit]
    return meters

if __name__ == '__main__':
    result_meters = convert_length(100, 'ft')
    print(result_meters)
    
    result_feet = convert_length(30.48, 'm') / 0.3048
    print(result_feet)
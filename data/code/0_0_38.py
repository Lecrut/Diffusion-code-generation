def convert_length(value: float, unit: str) -> float:
    conversions = {
        'm': 1.0,
        'ft': 0.3048,
        'cm': 0.01,
        'mm': 0.001,
        'km': 1000.0,
        'in': 0.0254,
        'yd': 0.9144,
        'mi': 1609.34,
    }
    
    unit_lower = unit.lower()
    
    if unit_lower not in conversions:
        raise ValueError(f"Unsupported unit: {unit}")
        
    meters = value * conversions[unit_lower]
    
    return meters

if __name__ == '__main__':
    result_meters = convert_length(10, 'm')
    print(result_meters)
    
    result_feet = convert_length(1, 'ft')
    print(result_feet)
    
    result_cm = convert_length(50, 'cm')
    print(result_cm)
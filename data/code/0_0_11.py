def convert_length(value: float, unit: str) -> float:
    units_to_meters = {
        'm': 1.0,
        'ft': 0.3048,
        'cm': 0.01,
        'in': 0.0254,
        'km': 1000.0,
        'mi': 1609.344,
        'mm': 0.001,
    }
    
    unit_lower = unit.lower()
    
    if unit_lower not in units_to_meters:
        raise ValueError(f"Unsupported unit: {unit}")
    
    meters = value * units_to_meters[unit_lower]
    
    return meters

if __name__ == '__main__':
    result = convert_length(10, 'ft')
    print(result)
def convert_distance(value: float, unit: str) -> dict:
    units = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'mi': 1609.344,
        'ft': 0.3048,
        'yd': 0.9144,
        'in': 0.0254
    }
    
    unit_lower = unit.lower()
    if unit_lower not in units:
        raise ValueError(f"Unsupported unit: {unit}")
    
    base_meters = value * units[unit_lower]
    
    return {
        k: base_meters / v for k, v in units.items()
    }

if __name__ == '__main__':
    sample_value = 5.0
    sample_unit = 'km'
    result = convert_distance(sample_value, sample_unit)
    print(f"Input: {sample_value} {sample_unit}")
    print("Converted values:")
    for u, v in result.items():
        print(f"  {u}: {v}")
def normalize_distance(value: float, unit: str) -> float:
    conversions = {
        'nm': 1e-9,
        'um': 1e-6,
        'mm': 1e-3,
        'cm': 1e-2,
        'dm': 1e-1,
        'm': 1,
        'km': 1e3,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.344,
        'nmi': 1852,
    }
    
    unit_lower = unit.lower()
    
    if unit_lower not in conversions:
        raise ValueError(f"Unsupported unit: {unit}")
    
    return value * conversions[unit_lower]

if __name__ == '__main__':
    result_meters = normalize_distance(1.0, 'km')
    print(result_meters)
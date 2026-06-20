UNIT_TO_METERS = {
    'm': 1.0,
    'km': 1000.0,
    'cm': 0.01,
    'mm': 0.001,
    'mi': 1609.344,
    'yd': 0.9144,
    'ft': 0.3048,
    'in': 0.0254,
    'nm': 1e-9,
}

SUPPORTED_UNITS = set(UNIT_TO_METERS.keys())

def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    if from_unit not in SUPPORTED_UNITS:
        raise ValueError(f"Unsupported source unit: {from_unit}")
    if to_unit not in SUPPORTED_UNITS:
        raise ValueError(f"Unsupported target unit: {to_unit}")
    
    meters = value * UNIT_TO_METERS[from_unit]
    result = meters / UNIT_TO_METERS[to_unit]
    return result

if __name__ == '__main__':
    result = convert_length(1, 'km', 'm')
    print(result)
    
    result = convert_length(1, 'mi', 'km')
    print(result)
    
    result = convert_length(12, 'in', 'cm')
    print(result)
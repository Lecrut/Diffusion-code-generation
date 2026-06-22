def convert_length(value: float, unit: str) -> float:
    units_to_meters = {
        'm': 1.0,
        'ft': 0.3048,
        'in': 0.0254,
        'cm': 0.01,
        'mm': 0.001,
    }
    
    if unit not in units_to_meters:
        raise ValueError(f"Unsupported unit: {unit}")
    
    meters = value * units_to_meters[unit]
    return meters

if __name__ == '__main__':
    print(convert_length(10, 'ft'))
    print(convert_length(100, 'cm'))
    print(convert_length(1, 'm'))
def convert_length(value: float, unit: str) -> float:
    conversions = {
        'm': 1.0,
        'ft': 0.3048,
        'cm': 0.01,
        'mm': 0.001,
        'km': 1000.0,
        'in': 0.0254,
        'yd': 0.9144,
    }
    
    if unit not in conversions:
        raise ValueError(f"Unsupported unit: {unit}")
        
    meters = value * conversions[unit]
    return meters

if __name__ == '__main__':
    print(convert_length(10, 'ft'))
    print(convert_length(5, 'm'))
    print(convert_length(100, 'cm'))
def convert_length(length: float, from_unit: str, to_unit: str) -> float:
    conversion_factors = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'ft': 0.3048,
        'in': 0.0254,
        'yd': 0.9144,
        'mi': 1609.344
    }
    
    from_factor = conversion_factors.get(from_unit)
    to_factor = conversion_factors.get(to_unit)
    
    if from_factor is None or to_factor is None:
        raise ValueError("Unsupported unit")
    
    meters = length * from_factor
    return meters / to_factor

if __name__ == '__main__':
    print(convert_length(1.0, 'm', 'ft'))
    print(convert_length(5.0, 'km', 'mi'))
    print(convert_length(100.0, 'cm', 'in'))
    print(convert_length(60.0, 'ft', 'm'))
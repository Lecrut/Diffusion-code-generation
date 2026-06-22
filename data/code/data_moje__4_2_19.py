def convert_distance(value: float, unit: str) -> dict:
    meters = 0.0
    if unit == 'm':
        meters = value
    elif unit == 'km':
        meters = value * 1000.0
    elif unit == 'mi':
        meters = value * 1609.344
    elif unit == 'ft':
        meters = value * 0.3048
    elif unit == 'in':
        meters = value * 0.0254
    else:
        raise ValueError(f"Unsupported unit: {unit}")
    
    return {
        'm': meters,
        'km': meters / 1000.0,
        'mi': meters / 1609.344,
        'ft': meters / 0.3048,
        'in': meters / 0.0254
    }

if __name__ == '__main__':
    sample_value = 1.0
    sample_unit = 'mi'
    result = convert_distance(sample_value, sample_unit)
    print(f"{sample_value} {sample_unit} = {result}")
    sample_value2 = 5.0
    sample_unit2 = 'km'
    result2 = convert_distance(sample_value2, sample_unit2)
    print(f"{sample_value2} {sample_unit2} = {result2}")
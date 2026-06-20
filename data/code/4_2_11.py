def convert_distance(value: float, unit: str) -> dict:
    if unit == 'm':
        meters = value
    elif unit == 'km':
        meters = value * 1000
    elif unit == 'mi':
        meters = value * 1609.344
    elif unit == 'ft':
        meters = value / 3.28084
    elif unit == 'in':
        meters = value / 39.3701
    elif unit == 'cm':
        meters = value / 100
    else:
        raise ValueError(f"Unsupported unit: {unit}")
    
    return {
        'm': meters,
        'km': meters / 1000,
        'mi': meters / 1609.344,
        'ft': meters * 3.28084,
        'in': meters * 39.3701,
        'cm': meters * 100
    }

if __name__ == '__main__':
    sample_value = 5.0
    sample_unit = 'mi'
    results = convert_distance(sample_value, sample_unit)
    print(results)
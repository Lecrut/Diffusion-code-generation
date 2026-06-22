def convert_length(value_str: str, target_unit: str) -> float:
    units_to_meters = {
        'm': 1.0,
        'ft': 0.3048,
        'in': 0.0254,
        'cm': 0.01,
        'mm': 0.001,
        'km': 1000.0,
        'yd': 0.9144,
        'mi': 1609.344,
    }

    if target_unit not in units_to_meters:
        raise ValueError(f"Unsupported target unit: {target_unit}")

    value_str = value_str.strip()
    try:
        if value_str.endswith('m'):
            val = float(value_str[:-1])
            source_unit = 'm'
        elif value_str.endswith('ft'):
            val = float(value_str[:-2])
            source_unit = 'ft'
        elif value_str.endswith('in'):
            val = float(value_str[:-2])
            source_unit = 'in'
        elif value_str.endswith('cm'):
            val = float(value_str[:-2])
            source_unit = 'cm'
        elif value_str.endswith('mm'):
            val = float(value_str[:-2])
            source_unit = 'mm'
        elif value_str.endswith('km'):
            val = float(value_str[:-2])
            source_unit = 'km'
        elif value_str.endswith('yd'):
            val = float(value_str[:-2])
            source_unit = 'yd'
        elif value_str.endswith('mi'):
            val = float(value_str[:-2])
            source_unit = 'mi'
        else:
            raise ValueError("Could not determine unit from string")
    except ValueError as e:
        if "could not convert" in str(e) or "unsupported literal" in str(e):
            raise ValueError(f"Invalid numeric value in string: {value_str}")
        raise

    meters = val * units_to_meters[source_unit]
    result = meters / units_to_meters[target_unit]
    
    return result

if __name__ == '__main__':
    print(convert_length("10m", 'ft'))
    print(convert_length("5.28ft", 'm'))
    print(convert_length("1km", 'mi'))
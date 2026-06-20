def convert_length(length_str, target_unit):
    conversions = {
        ('m', 'ft'): 3.28084,
        ('ft', 'm'): 0.3048,
        ('m', 'in'): 39.3701,
        ('in', 'm'): 0.0254,
        ('ft', 'in'): 12,
        ('in', 'ft'): 0.0833333,
        ('m', 'km'): 0.001,
        ('km', 'm'): 1000,
        ('ft', 'mi'): 0.000189394,
        ('mi', 'ft'): 5280,
        ('m', 'mi'): 0.000621371,
        ('mi', 'm'): 1609.34,
    }
    
    length_str = length_str.strip()
    try:
        value = float(length_str)
    except ValueError:
        raise ValueError(f"Invalid number format: {length_str}")
    
    source_unit = None
    for unit_code in ['ft', 'in', 'm', 'km', 'mi']:
        if length_str.endswith(unit_code):
            source_unit = unit_code
            numeric_part = length_str[: -len(unit_code)].strip()
            value = float(numeric_part)
            break
    
    if source_unit is None:
        source_unit = 'm'
        numeric_part = length_str.strip()
        value = float(numeric_part)
    
    if source_unit == target_unit:
        return f"{value} {target_unit}"
    
    if (source_unit, target_unit) in conversions:
        result = value * conversions[(source_unit, target_unit)]
        return f"{result:.4f} {target_unit}"
    
    raise ValueError(f"Conversion from {source_unit} to {target_unit} not supported")

if __name__ == '__main__':
    print(convert_length("10 m", "ft"))
    print(convert_length("5 ft", "in"))
    print(convert_length("1000 m", "km"))
    print(convert_length("3.5 mi", "m"))
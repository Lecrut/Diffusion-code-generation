def convert_length(value_str, target_unit_code):
    conversions = {
        ('ft', 'm'): 0.3048,
        ('in', 'm'): 0.0254,
        ('yd', 'm'): 0.9144,
        ('mi', 'm'): 1609.34,
        ('cm', 'm'): 0.01,
        ('mm', 'm'): 0.001,
        ('km', 'm'): 1000,
        ('m', 'ft'): 1 / 0.3048,
        ('m', 'in'): 1 / 0.0254,
        ('m', 'yd'): 1 / 0.9144,
        ('m', 'mi'): 1 / 1609.34,
        ('m', 'cm'): 100,
        ('m', 'mm'): 1000,
        ('m', 'km'): 0.001,
    }
    if value_str is None:
        return None
    
    try:
        parts = value_str.strip().split()
        value = float(parts[0])
        unit_code = parts[1].lower() if len(parts) > 1 else 'm'
        
        if unit_code == target_unit_code:
            return value
        
        key = (unit_code, target_unit_code)
        if key in conversions:
            result = value * conversions[key]
            return result
        
    except ValueError:
        raise ValueError("Invalid length format")
    
    raise ValueError(f"Unknown conversion from {unit_code} to {target_unit_code}")

if __name__ == '__main__':
    sample_value = "10 ft"
    target = 'm'
    result = convert_length(sample_value, target)
    print(result)
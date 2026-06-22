def convert_volume(value, from_unit, to_unit):
    conversion_factors = {
        'liters': 1.0,
        'milliliters': 0.001,
        'cubic_meters': 1000.0,
        'gallons': 3.78541,
        'cubic_inches': 0.0163871
    }
    if from_unit not in conversion_factors:
        raise ValueError(f"Unknown unit: {from_unit}")
    if to_unit not in conversion_factors:
        raise ValueError(f"Unknown unit: {to_unit}")
    
    liters_value = value * conversion_factors[from_unit]
    result = liters_value / conversion_factors[to_unit]
    return result

if __name__ == '__main__':
    sample_conversions = [
        (1.0, 'liters', 'gallons'),
        (1000.0, 'milliliters', 'liters'),
        (1.0, 'cubic_meters', 'liters'),
        (5.0, 'gallons', 'liters'),
        (100.0, 'cubic_inches', 'milliliters')
    ]
    
    for val, from_u, to_u in sample_conversions:
        result = convert_volume(val, from_u, to_u)
        print(f"{val} {from_u} = {result} {to_u}")
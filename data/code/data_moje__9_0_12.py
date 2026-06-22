def convert_volume(value, from_unit, to_unit):
    conversion_factors = {
        'liter': 1.0,
        'milliliter': 0.001,
        'cubic_meter': 1000.0,
        'gallon': 3.78541,
        'cubic_inch': 0.0163871
    }
    
    if from_unit not in conversion_factors:
        raise ValueError(f"Unsupported source unit: {from_unit}")
    
    if to_unit not in conversion_factors:
        raise ValueError(f"Unsupported target unit: {to_unit}")
    
    liters_value = value * conversion_factors[from_unit]
    result_value = liters_value / conversion_factors[to_unit]
    
    return result_value

if __name__ == '__main__':
    sample_conversions = [
        (1.0, 'liter', 'milliliter'),
        (1000.0, 'milliliter', 'liter'),
        (1.0, 'cubic_meter', 'liter'),
        (1.0, 'gallon', 'liter'),
        (1.0, 'cubic_inch', 'milliliter'),
        (2.5, 'gallon', 'cubic_inch'),
        (5.0, 'liter', 'gallon')
    ]
    
    for value, from_u, to_u in sample_conversions:
        result = convert_volume(value, from_u, to_u)
        print(f"{value} {from_u} = {result} {to_u}")
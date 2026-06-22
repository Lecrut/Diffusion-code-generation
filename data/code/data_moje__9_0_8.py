def convert_volume(value, from_unit, to_unit):
    conversion_factors = {
        'liter': 1.0,
        'milliliter': 0.001,
        'cubic_meter': 1000.0,
        'gallon': 3.78541,
        'cubic_inch': 0.0163871
    }
    if from_unit not in conversion_factors:
        raise ValueError(f"Unknown unit: {from_unit}")
    if to_unit not in conversion_factors:
        raise ValueError(f"Unknown unit: {to_unit}")
    
    liters = value * conversion_factors[from_unit]
    result = liters / conversion_factors[to_unit]
    return result

def main():
    sample_values = [
        (1, 'liter', 'gallon'),
        (500, 'milliliter', 'cubic_inch'),
        (2.5, 'cubic_meter', 'liter'),
        (10, 'gallon', 'milliliter'),
        (1, 'cubic_inch', 'liter')
    ]
    
    for value, from_unit, to_unit in sample_values:
        result = convert_volume(value, from_unit, to_unit)
        print(f"{value} {from_unit} = {result} {to_unit}")

if __name__ == '__main__':
    main()
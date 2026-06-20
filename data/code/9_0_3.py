def convert_volume(value: float, from_unit: str, to_unit: str) -> float:
    conversion_factors = {
        'liter': 1.0,
        'milliliter': 0.001,
        'cubic_meter': 1000.0,
        'gallon': 3.78541,
        'cubic_inch': 0.0163871
    }
    
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Unsupported unit")
    
    value_in_liters = value * conversion_factors[from_unit]
    result = value_in_liters / conversion_factors[to_unit]
    return result

def main():
    sample_cases = [
        (1000, 'milliliter', 'liter'),
        (1, 'cubic_meter', 'liter'),
        (1, 'gallon', 'liter'),
        (1, 'gallon', 'milliliter'),
        (100, 'cubic_inch', 'liter'),
        (10, 'liter', 'gallon'),
        (500, 'milliliter', 'cubic_inch')
    ]
    
    for value, from_unit, to_unit in sample_cases:
        result = convert_volume(value, from_unit, to_unit)
        print(f"{value} {from_unit} = {result} {to_unit}")

if __name__ == '__main__':
    main()
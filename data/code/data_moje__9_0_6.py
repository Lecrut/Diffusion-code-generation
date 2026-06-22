def convert_volume(value, from_unit, to_unit):
    liters_per_unit = {
        'liter': 1.0,
        'milliliter': 0.001,
        'cubic_meter': 1000.0,
        'gallon': 3.785411784,
        'cubic_inch': 0.016387064
    }
    
    if from_unit not in liters_per_unit or to_unit not in liters_per_unit:
        raise ValueError(f"Unsupported unit: {from_unit} or {to_unit}")
    
    liters = value * liters_per_unit[from_unit]
    result = liters / liters_per_unit[to_unit]
    return result

def main():
    test_cases = [
        (1.0, 'liter', 'milliliter'),
        (1000.0, 'milliliter', 'liter'),
        (1.0, 'cubic_meter', 'liter'),
        (1.0, 'gallon', 'liter'),
        (1.0, 'liter', 'gallon'),
        (100.0, 'cubic_inch', 'milliliter'),
        (5.0, 'liter', 'cubic_inch'),
        (1.0, 'cubic_meter', 'cubic_inch'),
        (10.0, 'gallon', 'cubic_inch'),
        (1.0, 'cubic_inch', 'cubic_meter')
    ]
    
    for value, from_unit, to_unit in test_cases:
        result = convert_volume(value, from_unit, to_unit)
        print(f"{value} {from_unit} = {result} {to_unit}")

if __name__ == '__main__':
    main()
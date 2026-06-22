CONVERSION_FACTORS = {
    'liters': 1.0,
    'milliliters': 0.001,
    'cubic_meters': 1000.0,
    'gallons': 3.78541,
    'cubic_inches': 0.0163871
}

def convert_volume(value, from_unit, to_unit):
    from_factor = CONVERSION_FACTORS.get(from_unit.lower())
    to_factor = CONVERSION_FACTORS.get(to_unit.lower())
    
    if from_factor is None or to_factor is None:
        raise ValueError(f"Unsupported unit. Supported units: {list(CONVERSION_FACTORS.keys())}")
    
    liters_value = value * from_factor
    result = liters_value / to_factor
    return result

def main():
    sample_conversions = [
        (1.0, 'liters', 'gallons'),
        (500.0, 'milliliters', 'cubic_inches'),
        (1.0, 'cubic_meters', 'liters'),
        (10.0, 'gallons', 'cubic_meters'),
        (100.0, 'cubic_inches', 'milliliters')
    ]
    
    for value, from_unit, to_unit in sample_conversions:
        result = convert_volume(value, from_unit, to_unit)
        print(f"{value} {from_unit} = {result} {to_unit}")

if __name__ == '__main__':
    main()
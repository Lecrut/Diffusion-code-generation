def convert_volume(value, from_unit, to_unit):
    conversions = {
        'liters': 1.0,
        'milliliters': 0.001,
        'cubic_meters': 1000.0,
        'gallons': 3.78541,
        'cubic_inches': 0.0163871
    }
    value_in_liters = value * conversions[from_unit.lower()]
    result = value_in_liters / conversions[to_unit.lower()]
    return result

def main():
    sample_values = [
        (1, 'liters', 'gallons'),
        (1, 'gallons', 'liters'),
        (500, 'milliliters', 'cubic_inches'),
        (1, 'cubic_meters', 'liters'),
        (100, 'cubic_inches', 'milliliters')
    ]
    for amount, source_unit, target_unit in sample_values:
        converted = convert_volume(amount, source_unit, target_unit)
        print(f"{amount} {source_unit} = {converted} {target_unit}")

if __name__ == '__main__':
    main()
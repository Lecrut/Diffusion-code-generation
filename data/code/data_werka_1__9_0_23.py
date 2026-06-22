def convert_volume(value, from_unit, to_unit):
    conversion_factors = {
        'liters_to_milliliters': 1000,
        'milliliters_to_liters': 0.001,
        'liters_to_cubic_meters': 0.001,
        'cubic_meters_to_liters': 1000,
        'liters_to_gallons': 0.264172,
        'gallons_to_liters': 3.78541,
        'liters_to_cubic_inches': 61.0237,
        'cubic_inches_to_liters': 0.0163871,
        'milliliters_to_cubic_meters': 0.000001,
        'cubic_meters_to_milliliters': 1000000,
        'milliliters_to_gallons': 0.000264172,
        'gallons_to_milliliters': 3785.41,
        'milliliters_to_cubic_inches': 0.0610237,
        'cubic_inches_to_milliliters': 16.3871,
        'cubic_meters_to_gallons': 264.172,
        'gallons_to_cubic_meters': 0.00378541,
        'cubic_meters_to_cubic_inches': 61023.7,
        'cubic_inches_to_cubic_meters': 0.0000163871
    }
    
    key = f"{from_unit.lower()}_to_{to_unit.lower()}"
    if key in conversion_factors:
        return value * conversion_factors[key]
    else:
        raise ValueError("Unsupported unit conversion")

if __name__ == '__main__':
    sample_values = [
        (5, 'liters', 'milliliters'),
        (2000, 'milliliters', 'liters'),
        (1.5, 'cubic meters', 'liters'),
        (3, 'gallons', 'liters'),
        (100, 'cubic inches', 'liters')
    ]
    
    for value, from_unit, to_unit in sample_values:
        result = convert_volume(value, from_unit, to_unit)
        print(f"{value} {from_unit} is {result} {to_unit}")
def convert_volume(value, from_unit, to_unit):
    conversion_factors = {
        'liters_to_milliliters': 1000,
        'milliliters_to_liters': 0.001,
        'liters_to_cubic_meters': 0.001,
        'cubic_meters_to_liters': 1000,
        'gallons_to_liters': 3.78541,
        'liters_to_gallons': 0.264172,
        'cubic_inches_to_liters': 0.0163871,
        'liters_to_cubic_inches': 61.0237,
        'gallons_to_cubic_inches': 231,
        'cubic_inches_to_gallons': 0.004329
    }
    
    key = f"{from_unit}_to_{to_unit}"
    if key in conversion_factors:
        return value * conversion_factors[key]
    else:
        raise ValueError("Invalid unit conversion")

if __name__ == '__main__':
    sample_values = [
        (1, 'liters', 'milliliters'),
        (500, 'milliliters', 'liters'),
        (2, 'cubic_meters', 'liters'),
        (3.78541, 'gallons', 'liters'),
        (61.0237, 'liters', 'cubic_inches')
    ]
    
    for value, from_unit, to_unit in sample_values:
        result = convert_volume(value, from_unit, to_unit)
        print(f"{value} {from_unit} is {result:.4f} {to_unit}")
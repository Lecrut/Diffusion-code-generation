def convert_volume(value, from_unit, to_unit):
    conversion_factors = {'liters_to_milliliters': 1000, 'milliliters_to_liters': 0.001, 'liters_to_cubic_meters': 0.001, 'cubic_meters_to_liters': 1000, 'gallons_to_liters': 3.78541, 'liters_to_gallons': 0.264172, 'cubic_inches_to_liters': 0.0163871, 'liters_to_cubic_inches': 61.0237, 'gallons_to_cubic_inches': 231, 'cubic_inches_to_gallons': 0.004329, 'cubic_meters_to_cubic_inches': 61023.7, 'cubic_inches_to_cubic_meters': 1.63871e-05}
    key = f'{from_unit.lower()}_to_{to_unit.lower()}'
    if key in conversion_factors:
        return value * conversion_factors[key]
    else:
        raise ValueError('Unsupported conversion')
if __name__ == '__main__':
    print(convert_volume(1, 'liters', 'milliliters'))
    print(convert_volume(1000, 'milliliters', 'liters'))
    print(convert_volume(1, 'cubic meters', 'liters'))
    print(convert_volume(1000, 'liters', 'cubic meters'))
    print(convert_volume(1, 'gallons', 'liters'))
    print(convert_volume(3.78541, 'liters', 'gallons'))
    print(convert_volume(1, 'cubic inches', 'liters'))
    print(convert_volume(0.0163871, 'liters', 'cubic inches'))
    print(convert_volume(1, 'gallons', 'cubic inches'))
    print(convert_volume(231, 'cubic inches', 'gallons'))
    print(convert_volume(1, 'cubic meters', 'cubic inches'))
    print(convert_volume(61023.7, 'cubic inches', 'cubic meters'))
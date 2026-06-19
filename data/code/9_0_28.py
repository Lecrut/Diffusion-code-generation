def convert_volume(value, from_unit, to_unit):
    conversion_factors = {'liters_to_milliliters': 1000, 'milliliters_to_liters': 0.001, 'liters_to_cubic_meters': 0.001, 'cubic_meters_to_liters': 1000, 'liters_to_gallons': 0.264172, 'gallons_to_liters': 3.78541, 'liters_to_cubic_inches': 61.0237, 'cubic_inches_to_liters': 0.0163871}
    conversion_key = f'{from_unit}_to_{to_unit}'
    if conversion_key in conversion_factors:
        return value * conversion_factors[conversion_key]
    else:
        raise ValueError('Unsupported conversion')

def main():
    print(convert_volume(1, 'liters', 'milliliters'))
    print(convert_volume(1000, 'milliliters', 'liters'))
    print(convert_volume(1, 'liters', 'cubic_meters'))
    print(convert_volume(1, 'cubic_meters', 'liters'))
    print(convert_volume(1, 'liters', 'gallons'))
    print(convert_volume(1, 'gallons', 'liters'))
    print(convert_volume(1, 'liters', 'cubic_inches'))
    print(convert_volume(1, 'cubic_inches', 'liters'))
if __name__ == '__main__':
    main()
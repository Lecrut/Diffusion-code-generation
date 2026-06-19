def convert_volume(value, from_unit, to_unit):
    conversion_factors = {'liters_to_milliliters': 1000, 'milliliters_to_liters': 0.001, 'liters_to_cubic_meters': 0.001, 'cubic_meters_to_liters': 1000, 'gallons_to_liters': 3.78541, 'liters_to_gallons': 0.264172, 'cubic_inches_to_liters': 0.0163871, 'liters_to_cubic_inches': 61.0237, 'gallons_to_cubic_inches': 231, 'cubic_inches_to_gallons': 0.004329}
    key = f'{from_unit}_to_{to_unit}'
    if key in conversion_factors:
        return value * conversion_factors[key]
    else:
        raise ValueError('Unsupported conversion')

def main():
    print(convert_volume(1, 'liters', 'milliliters'))
    print(convert_volume(2, 'gallons', 'liters'))
    print(convert_volume(3, 'cubic_meters', 'liters'))
    print(convert_volume(4, 'milliliters', 'liters'))
    print(convert_volume(5, 'gallons', 'cubic_inches'))
if __name__ == '__main__':
    main()
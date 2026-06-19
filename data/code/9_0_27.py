def convert_volume(value, from_unit, to_unit):
    conversion_factors = {'liters': 1, 'milliliters': 0.001, 'cubic_meters': 0.001, 'gallons': 0.264172, 'cubic_inches': 61.0237}
    value_in_liters = value * conversion_factors[from_unit]
    converted_value = value_in_liters / conversion_factors[to_unit]
    return converted_value
if __name__ == '__main__':
    print(convert_volume(10, 'liters', 'milliliters'))
    print(convert_volume(5, 'gallons', 'cubic_meters'))
    print(convert_volume(2000, 'milliliters', 'liters'))
    print(convert_volume(1, 'cubic_inches', 'gallons'))
    print(convert_volume(0.5, 'cubic_meters', 'liters'))
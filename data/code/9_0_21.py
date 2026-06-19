def convert_volume(value, from_unit, to_unit):
    conversion_factors = {'liters': 1, 'milliliters': 0.001, 'cubic meters': 0.001, 'gallons': 0.264172, 'cubic inches': 61.0237}
    value_in_liters = value * conversion_factors[from_unit]
    converted_value = value_in_liters / conversion_factors[to_unit]
    return converted_value
if __name__ == '__main__':
    print(convert_volume(1, 'liters', 'milliliters'))
    print(convert_volume(2, 'gallons', 'liters'))
    print(convert_volume(3, 'cubic meters', 'cubic inches'))
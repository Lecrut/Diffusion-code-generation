def convert_units(value, from_unit, to_unit, conversion_factors):
    if from_unit not in conversion_factors:
        raise ValueError(f'Conversion factor for {from_unit} is not defined.')
    if to_unit not in conversion_factors:
        raise ValueError(f'Conversion factor for {to_unit} is not defined.')
    base_value = value * conversion_factors[from_unit]
    converted_value = base_value / conversion_factors[to_unit]
    return converted_value
if __name__ == '__main__':
    conversion_factors = {'meters': 1.0, 'centimeters': 0.01, 'inches': 0.0254, 'feet': 0.3048, 'yards': 0.9144, 'kilometers': 1000.0, 'miles': 1609.34}
    value = 100
    from_unit = 'centimeters'
    to_unit = 'meters'
    result = convert_units(value, from_unit, to_unit, conversion_factors)
    print(result)
    value = 5
    from_unit = 'miles'
    to_unit = 'kilometers'
    result = convert_units(value, from_unit, to_unit, conversion_factors)
    print(result)
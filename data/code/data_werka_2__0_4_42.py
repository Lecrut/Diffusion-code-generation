def convert_units(value, from_unit, to_unit, conversion_factors):
    if from_unit not in conversion_factors:
        raise ValueError(f'Conversion factor for {from_unit} is not defined.')
    if to_unit not in conversion_factors:
        raise ValueError(f'Conversion factor for {to_unit} is not defined.')
    base_value = value * conversion_factors[from_unit]
    converted_value = base_value / conversion_factors[to_unit]
    return converted_value
if __name__ == '__main__':
    conversion_factors = {'meters': 1.0, 'centimeters': 0.01, 'inches': 0.0254, 'feet': 0.3048, 'yards': 0.9144, 'miles': 1609.34}
    value = 100
    from_unit = 'centimeters'
    to_unit = 'feet'
    result = convert_units(value, from_unit, to_unit, conversion_factors)
    print(f'{value} {from_unit} is equal to {result:.2f} {to_unit}')
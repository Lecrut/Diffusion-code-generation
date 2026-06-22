def get_conversion_factors():
    return {'feet_to_inches': 12.0}

def convert_units(value, from_unit, to_unit, factors):
    if to_unit != 'inches':
        raise ValueError(f"Unsupported target unit: {to_unit}")
    if from_unit != 'feet':
        raise ValueError(f"Unsupported source unit: {from_unit}")
    factor = factors['feet_to_inches']
    return value * factor

def feet_to_inches(feet):
    factors = get_conversion_factors()
    return convert_units(feet, 'feet', 'inches', factors)

if __name__ == '__main__':
    sample_feet_values = [0, 1, 5, 10.5, 100]
    for value in sample_feet_values:
        result = feet_to_inches(value)
        print(result)
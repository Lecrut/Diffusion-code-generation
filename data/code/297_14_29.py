conversion_factors = {
    'inches_to_cm': 2.54,
    'cm_to_inches': 1 / 2.54
}

def validate_unit(unit):
    if unit not in conversion_factors:
        raise ValueError(f"Invalid unit: {unit}. Supported units are 'inches' and 'cm'.")

def convert(value, from_unit, to_unit):
    validate_unit(from_unit)
    validate_unit(to_unit)
    return value * conversion_factors[f'{from_unit}_to_{to_unit}']

if __name__ == '__main__':
    print(convert(1, 'inches', 'cm'))
    print(convert(0.5, 'inches', 'cm'))
    print(convert(2.54, 'cm', 'inches'))
    print(convert(12.7, 'cm', 'inches'))
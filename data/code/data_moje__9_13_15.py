CONVERSION_FACTORS = {
    'mL_to_L': 0.001,
    'L_to_mL': 1000.0,
    'm3_to_L': 1000.0,
    'L_to_m3': 0.001,
    'gal_to_L': 3.78541,
    'L_to_gal': 0.264172
}

def convert_volume(value: float, from_unit: str, to_unit: str) -> float:
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit == to_unit:
        return value

    if from_unit == 'ml' and to_unit == 'l':
        return value * CONVERSION_FACTORS['mL_to_L']
    if from_unit == 'l' and to_unit == 'ml':
        return value * CONVERSION_FACTORS['L_to_mL']
    if from_unit == 'm3' and to_unit == 'l':
        return value * CONVERSION_FACTORS['m3_to_L']
    if from_unit == 'l' and to_unit == 'm3':
        return value * CONVERSION_FACTORS['L_to_m3']
    if from_unit == 'gal' and to_unit == 'l':
        return value * CONVERSION_FACTORS['gal_to_L']
    if from_unit == 'l' and to_unit == 'gal':
        return value * CONVERSION_FACTORS['L_to_gal']
    if from_unit == 'ml' and to_unit == 'm3':
        l_value = value * CONVERSION_FACTORS['mL_to_L']
        return l_value * CONVERSION_FACTORS['L_to_m3']
    if from_unit == 'm3' and to_unit == 'ml':
        l_value = value * CONVERSION_FACTORS['m3_to_L']
        return l_value * CONVERSION_FACTORS['L_to_mL']
    if from_unit == 'ml' and to_unit == 'gal':
        l_value = value * CONVERSION_FACTORS['mL_to_L']
        return l_value * CONVERSION_FACTORS['L_to_gal']
    if from_unit == 'gal' and to_unit == 'ml':
        l_value = value * CONVERSION_FACTORS['gal_to_L']
        return l_value * CONVERSION_FACTORS['L_to_mL']
    if from_unit == 'm3' and to_unit == 'gal':
        l_value = value * CONVERSION_FACTORS['m3_to_L']
        return l_value * CONVERSION_FACTORS['L_to_gal']
    if from_unit == 'gal' and to_unit == 'm3':
        l_value = value * CONVERSION_FACTORS['gal_to_L']
        return l_value * CONVERSION_FACTORS['L_to_m3']

    raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}")

if __name__ == '__main__':
    sample_ml = 500.0
    sample_l = 1.5
    sample_m3 = 0.002
    sample_gal = 1.0

    print(convert_volume(sample_ml, 'ml', 'l'))
    print(convert_volume(sample_l, 'l', 'ml'))
    print(convert_volume(sample_m3, 'm3', 'l'))
    print(convert_volume(sample_l, 'l', 'm3'))
    print(convert_volume(sample_gal, 'gal', 'l'))
    print(convert_volume(sample_l, 'l', 'gal'))
    print(convert_volume(sample_ml, 'ml', 'm3'))
    print(convert_volume(sample_m3, 'm3', 'ml'))
    print(convert_volume(sample_ml, 'ml', 'gal'))
    print(convert_volume(sample_gal, 'gal', 'ml'))
    print(convert_volume(sample_m3, 'm3', 'gal'))
    print(convert_volume(sample_gal, 'gal', 'm3'))
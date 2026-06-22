def convert_to_liters(volume, unit):
    ML_TO_L = 0.001
    CL_TO_L = 0.01
    DL_TO_L = 0.1
    FL_OZ_TO_L = 0.0295735296
    CUP_TO_L = 0.2365882365
    PT_TO_L = 0.473176473
    QT_TO_L = 0.946352946
    GAL_TO_L = 3.785411784
    conversion_factors = {'ml': ML_TO_L, 'cl': CL_TO_L, 'dl': DL_TO_L, 'l': 1.0, 'fl oz': FL_OZ_TO_L, 'cup': CUP_TO_L, 'pt': PT_TO_L, 'qt': QT_TO_L, 'gal': GAL_TO_L}
    if unit.lower() not in conversion_factors:
        raise ValueError(f'Unsupported unit: {unit}')
    return volume * conversion_factors[unit.lower()]
if __name__ == '__main__':
    sample_values = [(100, 'ml'), (500, 'cl'), (2, 'dl'), (1, 'l'), (8, 'fl oz'), (2, 'cup'), (1, 'pt'), (1, 'qt'), (1, 'gal')]
    for volume, unit in sample_values:
        result = convert_to_liters(volume, unit)
        print(f'{volume} {unit} is equal to {result} liters')
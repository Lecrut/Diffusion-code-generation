def convert_to_liters(volume, unit):
    ML_TO_LITERS = 1e-3
    CL_TO_LITERS = 1e-2
    DL_TO_LITERS = 1e-1
    LITERS_TO_LITERS = 1.0
    FL_OZ_TO_LITERS = 0.0295735296
    CUP_TO_LITERS = 0.2365882365
    PT_TO_LITERS = 0.473176473
    QT_TO_LITERS = 0.946352946
    GAL_TO_LITERS = 3.785411784

    conversion_factors = {
        'ml': ML_TO_LITERS,
        'cl': CL_TO_LITERS,
        'dl': DL_TO_LITERS,
        'l': LITERS_TO_LITERS,
        'fl oz': FL_OZ_TO_LITERS,
        'cup': CUP_TO_LITERS,
        'pt': PT_TO_LITERS,
        'qt': QT_TO_LITERS,
        'gal': GAL_TO_LITERS
    }

    if unit.lower() not in conversion_factors:
        raise ValueError(f"Unsupported unit: {unit}")
    return volume * conversion_factors[unit.lower()]

if __name__ == '__main__':
    sample_values = [
        (100, 'ml'),
        (50, 'cl'),
        (2, 'dl'),
        (1, 'l'),
        (8, 'fl oz'),
        (2, 'cup'),
        (1, 'pt'),
        (1, 'qt'),
        (1, 'gal')
    ]

    for volume, unit in sample_values:
        print(f"{volume} {unit} is {convert_to_liters(volume, unit)} liters")
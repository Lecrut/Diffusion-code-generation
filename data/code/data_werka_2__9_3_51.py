class VolumeConverter:
    ML_TO_LITERS = 1e-3
    CL_TO_LITERS = 1e-2
    DL_TO_LITERS = 1e-1
    FL_OZ_TO_LITERS = 0.0295735296
    CUP_TO_LITERS = 0.2365882365
    PT_TO_LITERS = 0.473176473
    QT_TO_LITERS = 0.946352946
    GAL_TO_LITERS = 3.785411784

    @staticmethod
    def convert_to_liters(volume, unit):
        conversion_factors = {
            'ml': VolumeConverter.ML_TO_LITERS,
            'cl': VolumeConverter.CL_TO_LITERS,
            'dl': VolumeConverter.DL_TO_LITERS,
            'l': 1.0,
            'fl oz': VolumeConverter.FL_OZ_TO_LITERS,
            'cup': VolumeConverter.CUP_TO_LITERS,
            'pt': VolumeConverter.PT_TO_LITERS,
            'qt': VolumeConverter.QT_TO_LITERS,
            'gal': VolumeConverter.GAL_TO_LITERS
        }
        if unit.lower() not in conversion_factors:
            raise ValueError(f"Unsupported unit: {unit}")
        return volume * conversion_factors[unit.lower()]

if __name__ == '__main__':
    sample_values = [
        (100, 'ml'),
        (50, 'cl'),
        (20, 'dl'),
        (1, 'l'),
        (8, 'fl oz'),
        (2, 'cup'),
        (1, 'pt'),
        (1, 'qt'),
        (1, 'gal')
    ]

    for volume, unit in sample_values:
        print(f"{volume} {unit} is {VolumeConverter.convert_to_liters(volume, unit)} liters")
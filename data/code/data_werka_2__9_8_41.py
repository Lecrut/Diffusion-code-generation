class VolumeConverter:
    LITERS_TO_MILLILITERS = 1000
    LITERS_TO_CUBIC_METERS = 0.001
    MILLILITERS_TO_LITERS = 0.001
    MILLILITERS_TO_CUBIC_METERS = 1e-06
    CUBIC_METERS_TO_LITERS = 1000
    CUBIC_METERS_TO_MILLILITERS = 1000000

    CONVERSION_RATES = {
        'liters': {'liters': 1, 'milliliters': LITERS_TO_MILLILITERS, 'cubic_meters': LITERS_TO_CUBIC_METERS},
        'milliliters': {'liters': MILLILITERS_TO_LITERS, 'milliliters': 1, 'cubic_meters': MILLILITERS_TO_CUBIC_METERS},
        'cubic_meters': {'liters': CUBIC_METERS_TO_LITERS, 'milliliters': CUBIC_METERS_TO_MILLILITERS, 'cubic_meters': 1}
    }

    @staticmethod
    def convert_volume(volume, source_unit, target_unit='liters'):
        if source_unit not in VolumeConverter.CONVERSION_RATES:
            raise ValueError(f"Unsupported source unit: {source_unit}")
        if target_unit not in VolumeConverter.CONVERSION_RATES[source_unit]:
            raise ValueError(f"Unsupported target unit from {source_unit}: {target_unit}")
        return volume * VolumeConverter.CONVERSION_RATES[source_unit][target_unit]

if __name__ == '__main__':
    sample_volume = 3
    sample_source_unit = 'liters'
    sample_target_unit = 'milliliters'
    converted_volume = VolumeConverter.convert_volume(sample_volume, sample_source_unit, sample_target_unit)
    print(f"{sample_volume} {sample_source_unit} is {converted_volume} {sample_target_unit}")

    sample_volume = 2000
    sample_source_unit = 'milliliters'
    sample_target_unit = 'cubic_meters'
    converted_volume = VolumeConverter.convert_volume(sample_volume, sample_source_unit, sample_target_unit)
    print(f"{sample_volume} {sample_source_unit} is {converted_volume} {sample_target_unit}")

    sample_volume = 1.5
    sample_source_unit = 'cubic_meters'
    sample_target_unit = 'liters'
    converted_volume = VolumeConverter.convert_volume(sample_volume, sample_source_unit, sample_target_unit)
    print(f"{sample_volume} {sample_source_unit} is {converted_volume} {sample_target_unit}")
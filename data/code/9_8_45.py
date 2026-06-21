def convert_volume(volume, source_unit, target_unit='liters'):
    conversion_rates = {
        'liters': {'liters': 1, 'milliliters': 1000, 'cubic_meters': 0.001},
        'milliliters': {'liters': 0.001, 'milliliters': 1, 'cubic_meters': 0.000001},
        'cubic_meters': {'liters': 1000, 'milliliters': 1000000, 'cubic_meters': 1}
    }
    if source_unit not in conversion_rates:
        raise ValueError(f"Unsupported source unit: {source_unit}")
    if target_unit not in conversion_rates[source_unit]:
        raise ValueError(f"Unsupported target unit from {source_unit}: {target_unit}")
    return volume * conversion_rates[source_unit][target_unit]

if __name__ == '__main__':
    sample_volume_1 = 5
    sample_source_unit_1 = 'liters'
    sample_target_unit_1 = 'milliliters'
    converted_volume_1 = convert_volume(sample_volume_1, sample_source_unit_1, sample_target_unit_1)
    print(f"{sample_volume_1} {sample_source_unit_1} is {converted_volume_1} {sample_target_unit_1}")

    sample_volume_2 = 500
    sample_source_unit_2 = 'milliliters'
    sample_target_unit_2 = 'cubic_meters'
    converted_volume_2 = convert_volume(sample_volume_2, sample_source_unit_2, sample_target_unit_2)
    print(f"{sample_volume_2} {sample_source_unit_2} is {converted_volume_2} {sample_target_unit_2}")

    sample_volume_3 = 2
    sample_source_unit_3 = 'cubic_meters'
    sample_target_unit_3 = 'liters'
    converted_volume_3 = convert_volume(sample_volume_3, sample_source_unit_3, sample_target_unit_3)
    print(f"{sample_volume_3} {sample_source_unit_3} is {converted_volume_3} {sample_target_unit_3}")